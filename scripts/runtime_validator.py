#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Set

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = json.loads((ROOT / 'src' / 'schemas' / 'task_contracts.json').read_text(encoding='utf-8'))
RULES = json.loads((ROOT / 'src' / 'schemas' / 'validation_rules.json').read_text(encoding='utf-8'))
STOPWORDS = {
    'the','a','an','and','or','to','of','in','on','for','with','is','are','be','this','that','it','as','by','from','at',
    'if','then','than','into','about','your','you','we','they','their','our','will','would','should','could','can','just',
    'very','really','more','most','some','any','all','not','do','does','did','so','but','because'
}
PLACEHOLDER_PHRASES = ['[placeholder]', '(placeholder)', 'placeholder here', 'insert placeholder',
                        'tbd', 'lorem ipsum', 'route is explicit',
                        'required sections are visible', 'evidence burden is named']
# NOTE: 'placeholder content' removed — fires on legitimate prose about HTML placeholder
# attributes (e.g. 'screen readers may announce placeholder content on some implementations')
SUPERLATIVES = [
    # Pure marketing puffery — no technical grounding possible
    'best-in-class', 'externally validated', 'industry-standard', 'battle-tested',
    'enterprise-grade', 'seamless', 'future-proof', 'cutting-edge', 'world-class',
    'bulletproof', 'foolproof', 'state-of-the-art',
    # Removed: 'validated', 'proven', 'certified', 'compliant', 'production-ready',
    # 'scalable', 'robust', 'maintainable', 'reliable', 'best-practice' —
    # these are legitimate technical words that fire false positives on grounded outputs
    # ('compliant with ARIA', 'robust transitions', 'reliable retry logic')
]
TRADEOFF_TOKENS = ['tradeoff', 'trade-off', 'instead of', 'rather than', 'preserve', 'sacrifice', 'compromise', 'flex first', 'tension', 'should win', 'you must choose', 'choosing between', 'versus', 'vs.', 'downside', 'upside', 'cost of', 'safe path', 'safer path', 'the risk is', 'the trade is', 'choosing', 'chose to', 'opted for', 'over the alternative', 'path forward', 'what to avoid', 'avoid this', 'prefer ', 'do not use', 'use instead', 'the downside', 'the catch', 'the benefit', 'watch out', 'avoid building', 'avoid adopting', 'risk:', 'bola', 'bfla', 'bounded staleness', 'not inline', 'do not rely', 'not via', 'latency', 'the tradeoff is', 'at the cost', 'in exchange', 'the downside is', 'this prevents', 'this avoids', 'the cost of this', 'the cost here', 'this means accepting', 'means giving up', 'you lose', 'you gain', 'what you give up', 'what you get back', 'one downside', 'the risk here', 'this approach costs', 'weighing', 'the tradeoff here', 'a key tradeoff', 'core tradeoff', 'primary tradeoff', 'accept the cost', 'bear the cost', 'the architecture cost', 'architecture tax', 'the overhead', 'the burden', 'you sacrifice', 'at the expense of', 'pros and cons', 'on the other hand', 'however this', 'but this', 'the catch is', 'the gotcha', 'the caveat', '**tradeoff', '**sacrificed', 'tradeoff:', 'sacrificed:', 'what changed:']
RATIONALE_TOKENS = ['because', 'so that', 'therefore', 'why', 'this matters', 'this is', 'this creates', 'this delays', 'this causes', 'this means', 'this prevents', 'this ensures', 'this violates', 'this fixes', 'this gates', 'in order to', 'as a result', 'without this', 'failure:', 'risk:', 'which means', 'when to use', 'not to use', 'does not own', 'must not', 'cannot', 'it does not', 'to prevent', 'to ensure', 'to handle', 'does not', 'is not a', 'to avoid', 'why this', 'why first', 'why parallel', 'why it', 'so the', 'this destroys', 'these destroy', 'this breaks', 'this loses', 'the reasoning', 'the reason to', 'the reason for', 'my reasoning', 'this is important because', 'this matters because', 'this is necessary', 'this is required', 'behind this', 'the logic behind', 'by doing so', 'in doing so', 'this allows', 'this enables', 'this forces', 'without which', 'failing to do so', 'if we do not', 'if you do not', 'the implication', 'the consequence', 'the impact is', 'the effect is', 'this way', 'doing this', 'by choosing', 'this choice', 'this decision', 'this approach', 'this strategy', 'this pattern', '**tradeoff', 'tradeoff:', '**because', 'what changed:', 'why i', 'why this works']
ALTERNATIVE_TOKENS = ['alternative', 'option b', 'instead', 'why not', 'obvious alternative']
GOVERNING_RULE_TOKENS = ['should win', 'wins', 'governing rule', 'priority', 'instead of', 'rather than', 'tradeoff', 'preserve']
STYLE_BLEED_TOKENS = ['palette', 'colorway', 'logo', 'poster', 'moodboard', 'brand color', 'font pairing', 'typeface personality', 'illustration style', 'make it pop', 'looks cool']
CONTRADICTION_PAIRS = [
    ('maximize density', 'reduce cognitive load'),
    ('preserve existing layout exactly', 'normalize grid aggressively'),
    ('do not ask the user for the grid', 'ask which grid they want'),
    ('evidence is missing', 'validated result'),
    ('side panel and modal should be merged', 'keep both patterns for same use case'),
    ('flatten the pdf', 'preserve semantics'),
    ('show everything above the fold', 'reduce cognitive load')
]
EVIDENCE_CLASS_PATTERNS = {
    'measurable_threshold': [r'\bthreshold\b', r'\bscore\b', r'\bmetric\b', r'\bbenchmark\b', r'\bwcag\b', r'\bapca\b', r'\b\d+(?:\.\d+)?%\b', r'\b\d+(?:\.\d+)?:1\b', r'\bkpi\b', r'\bkpis\b', r'\bconversion rate\b', r'\bdrop.?off\b'],
    'comparison_artifact': [r'\bbaseline\b', r'\bcomparison\b', r'\bcompare\b', r'\bversus\b', r'\bvs\b', r'\bbefore/after\b', r'\balternative\b', r'\bobvious alternative\b', r'\bcompetitor\b', r'\bcompetitors\b', r'\bagainst the\b', r'\bpositioned against\b', r'\bnot a\b', r'\bunlike\b', r'\boption [ab]\b', r'\binstead of\b', r'\brather than\b', r'\bswap\b', r'\bdemote\b', r'\bover\b', r'\breplace\b', r'\b(a|b):\b', r'\bcompetes\b', r'\bcompeting\b', r'\bthe original\b', r'\boriginal has\b', r'\bbefore revision\b', r'\bhere.s the revised\b', r'\bthe revision\b'],
    'state_or_behavior_rule': [r'\bstate\b', r'\bkeyboard\b', r'\bfocus\b', r'\bhierarchy\b', r'\bscan\b', r'\bflow\b', r'\border\b', r'\bbehavior\b', r'\bsequence\b', r'\bstate machine\b'],
    'implementation_constraint': [r'\bconstraint\b', r'\blimit\b', r'\bblocked\b', r'\bboundary\b', r'\brequires\b', r'\bdepends\b', r'\bonly if\b', r'\bpreserve\b', r'\bpreservat', r'\bsequencing\b', r'\bsafer path\b', r'\bintegration\b', r'\bdensity\b', r'\btoken\b', r'\balias\b', r'\bsemantic role\b', r'\bhex\b', r'\bgrid\b', r'\boverlay\b', r'\bhydration\b', r'\bbundle\b', r'\bconvention\b', r'\bcannot\b', r'\bmust not\b', r'\bnot safe\b', r'\bbreaking change\b',
        # GPT pre-flight, brand/trust, DeepSeek constraint-satisfaction
        r'\bpre-flight\b', r'\bpost-flight\b', r'\bcannot proceed\b', r'\birreversible\b',
        r'\brequire manual\b', r'\btrust without\b', r'\bcategory convention\b',
        r'\bconvention demands\b', r'\bstep-by-step verification\b', r'\bconstraint satisfaction\b',
        # New additions from batch analysis — brand, content, research constraint vocab
        r'\bonly works if\b', r'\bthis only holds\b', r'\bfails without\b',
        r'\bbreaks if\b', r'\bcannot claim\b', r'\btrust requires\b',
        r'\baudience requires\b', r'\bproof requires\b', r'\bthe constraint\b',
        r'\bbound by\b', r'\bconstrained by\b', r'\bmust come first\b',
        r'\bmust precede\b', r'\bbefore you can\b', r'\bstep \d+ must\b',
        r'\bphase \d+ before\b', r'\bsequence matters\b', r'\bthe order matters\b',
        r'\byou cannot skip\b', r'\bif you skip\b', r'\byou must first\b'],

    'file_backed_receipt': [r'\[file:', r'\bartifact\b', r'\blog\b', r'\bscorecard\b', r'\bfixture\b', r'\bvalidation result\b', r'\bsignal\b', r'\breceipt\b', r'\bproof comes\b', r'\breal signal\b', r'\btrust signal\b', r'\bmeasurement\b', r'\bbenchmark\b', r'\bopen gap\b', r'\bproof artifact\b', r'\bproof boundary\b', r'\bseparates proof\b', r'\basymmetric proof\b', r'\bproof move\b', r'\bproof burden\b', r'\bproof in\b', r'\bproof that\b', r'\bproof through\b',
        # Cross-model additions (Gemini/Nova RAG grounding vocabulary)
        r'\bverification signal\b', r'\breproducibility indicator\b', r'\bgrounding signal\b',
        r'\bbased on search results\b'],
    'benchmark_artifact': [r'\bbenchmark\b', r'\bscorecard\b', r'\beval\b', r'\bregression\b', r'\brun-\d+\b', r'\bbenchmark-run\b'],
    'reviewer_confidence_artifact': [r'\breviewer\b', r'\bconfidence\b', r'\bhuman review\b', r'\bexternal signal\b'],
    'standards_reference': [r'\bwcag\b', r'\bapca\b', r'\bpdf/ua\b', r'\baria\b', r'\bunicode\b', r'\breading order\b', r'\btag\b', r'\bartifact\b', r'\bcontrast\b', r'\brfc 9457\b', r'\bproblem details\b', r'\breact context\b', r'\bredux\b', r'\bhooks\b', r'\buse[a-z]+\b', r'\bdocumented\b', r'\bconvention\b', r'\bpattern\b', r'\bspec\b', r'\bstandard\b', r'\bbest practice\b'],
    'permission_rule': [r'\bauth\b', r'\bpermission\b', r'\brole\b', r'\baccess\b', r'\binvite\b', r'\brevocation\b', r'\bapproval\b', r'\bbola\b', r'\bbfla\b', r'\btenant\b', r'\bobject-level\b',
        # Cross-model additions (Llama ABAC, Qwen owner-only, Grok tenant, GPT pre-flight)
        r'\battribute-based access\b', r'\bdeny by default\b', r'\bowner-only\b',
        r'\benforce tenant\b', r'\bask permission only\b', r'\bauth handshake\b',
        r'\bobject-level permission\b', r'\bcheck for bola\b'],
    'data_model_dependency': [r'\bdata model\b', r'\bschema\b', r'\bownership\b', r'\bfield\b', r'\brecord\b', r'\bobject\b', r'\btenant\b', r'\bmembership\b', r'\bretention\b', r'\bsource-of-truth\b', r'\bcanonical\b'],
    'verification_method': [r'\bverify\b', r'\bverification\b', r'\bcheck\b', r'\btest\b', r'\binspect\b', r'\bcopy-paste\b', r'\bextract\b', r'\bscreen reader\b', r'\boverlay\b', r'\bmeasurement\b', r'\bcompare\b', r'\bkeyboard only\b', r'\baxe\b'],
    'narrative_proof_boundary': [r'\bclaim\b', r'\bproof\b', r'\bproxy\b', r'\bmeasured\b', r'\bevidence\b', r'\bopen gap\b', r'\bexternal\b', r'\binternal\b', r'\banalytics\b', r'\bmetrics showed\b', r'\bpost-launch\b', r'\bcohort\b', r'\bsplit sample\b', r'\binterview\b',
        # Cross-model additions (Mistral claim-vs-data, Grok EQ-uncertainty framing)
        r'\bclaim vs data\b', r'\bderived from metadata\b', r'\buser-stated requirements\b',
        r'\bverified conclusion\b'],
    'research_artifact': [r'\binterview\b', r'\bsurvey\b', r'\busability test\b', r'\bparticipant\b', r'\brespondent\b', r'\bsample\b', r'\btranscript\b', r'\bfield study\b', r'\bdiary\b', r'\bscreener\b'],
    'visual_structure_rule': [r'\bcomposition\b', r'\bfocal\b', r'\blegibility\b', r'\bdistance\b', r'\balignment\b', r'\brhythm\b', r'\bgrouping\b', r'\bscale\b', r'\bcontrast\b', r'\bproportion\b', r'\bthumbnail\b'],
    'rendering_boundary_rule': [r'\bserver component\b', r'\bclient component\b', r'\buse client\b', r'\bserver action\b', r'\bstatic\b', r'\bdynamic\b', r'\bppr\b', r'\bstreaming\b', r'\bsuspense\b', r'\bhydration\b', r'\bcomponent boundary\b', r'\brender boundary\b', r'\bprop drilling\b', r'\bconsumption breadth\b', r'\bcomponent tree\b', r'\bre-render\b', r'\bstate boundary\b', r'\blocal state\b', r'\bglobal state\b', r'\bstate scope\b', r'\bstate locality\b',
        # Cross-model additions (generic state management, Gemini visual-state vocabulary)
        r'\bcontext provider\b', r'\bvisual state persistence\b', r'\bsensory.rich interface\b'],
    'consistency_model': [r'\blinearizable\b', r'\bbounded staleness\b', r'\bread-your-writes\b',
        r'\brevision token\b', r'\bconsistency token\b', r'\bzedtoken\b',
        r'\bcursor\b', r'\bkeyset\b', r'\boutbox\b', r'\bmicro-batch\b',
        r'\bidempotent\b', r'\bupsert\b', r'\bno-op\b', r'\batomic\b',
        r'\bstored response\b', r'\bidempotency key\b',
        r'idempotency-key', r'\bttl\b', r'\bcached response\b',
        r'\bcache.*response\b', r'\bstore.*response\b',
        r'\breplay\b', r'\beventual consistency\b', r'\bstrong consistency\b',
        r'\bsource of truth\b', r'\bsingle source\b'],
    'failure_semantics_rule': [r'\brfc 9457\b', r'\bproblem details\b', r'\bapplication/problem\+json\b', r'\btype\b', r'\btitle\b', r'\bstatus\b', r'\bdetail\b', r'\binstance\b'],
    'async_lifecycle_rule': [r'\bidempotency-key\b', r'\bfingerprint\b', r'\b409 conflict\b', r'\b422 unprocessable\b', r'\b400 bad request\b', r'\b202 accepted\b', r'\bstatus url\b', r'\bqueued\b', r'\brunning\b', r'\bterminal failure\b', r'\bterminal success\b'],
    'meaning_preservation_guard': [r'\bmeaning-preservation\b', r'\bmeaning guard\b', r'\bclaims preserved\b', r'\bargument preserved\b', r'\bdrift risk\b', r'\bmust stay unchanged\b', r'\bclaim intact\b', r'\bnothing is lost\b', r'\bnothing lost\b', r'\bactual claim\b', r'\bkeeps the.*claim\b', r'\bpreserved\b', r'\bintact\b'],
    'prose_quality_signal': [r'\bpattern\b', r'\brepeated\b', r'\bformulaic\b', r'\bnominali', r'\btransition\b', r'\brhythm\b', r'\bverb logic\b', r'\bverb\b', r'\bvoice\b', r'\bauthored texture\b', r'\babstract\b', r'\bconcrete\b', r'\bword choice\b', r'\bsentence\b', r'\bphrasing\b', r'\bpadding\b', r'\bjargon\b', r'\bdense\b', r'\bplain\b', r'\bpassive\b', r'\bactive\b'],
    'tier_behavior_rule': [r'\bfunctional\b', r'\bintegrative\b', r'\bstrategic\b', r'\bjargon\b', r'\bscaffolding\b', r'\bnext step\b'],
    'next_step_guidance': [r'\bnext step\b', r'\bstart with\b', r'\bfirst move\b', r'\bsafer next move\b', r'\bthen\b'],
    'resilience_rule': [r'\bcircuit breaker\b', r'\bbackoff\b', r'\bjitter\b', r'\bload shedding\b', r'\bgraceful degradation\b', r'\bcache-fallback\b', r'\bquota\b', r'\brate limit\b', r'\btrace_id\b', r'\bobservability\b',
        # Cross-model additions (Nova AWS-native, Grok EQ-aware, Llama 4 sophisticated patterns)
        r'\bmttr\b', r'\bmean time to resolution\b', r'\bincident prevention\b',
        r'\bproactive response\b', r'\breliability metrics\b', r'\bexponential backoff\b',
        r'\bcircuit breaker threshold\b', r'\bgraceful degradation protocol\b'],
    # New class: RAG/retrieval grounding (Nova, Gemini Deep Research)
    'grounding_citation': [
        r'\bbased on search results\b', r'\bretrieved from\b', r'\bcitation \d+\b',
        r'\bper the \w+ (document|source|reference)\b',
        r'\bthe \w+ (report|file|pdf) (shows|indicates|states)\b',
        r'\bsemantic (pairs|analysis) (shows|reveals)\b',
        r'\bextracted metadata\b', r'\bcharacter-level comparison\b',
        r'\bthe attached\b', r'\bsection \d+ indicates\b',
    ],
}
SPECIFICITY_PATTERNS = [
    r'\b\d+(?:\.\d+)?\s?(?:px|pt|ms|s|seconds?|minutes?|hours?)\b',
    r'\b\d+(?:\.\d+)?:1\b',
    r'\bthreshold\b',
    r'\bscore\b',
    r'\bbenchmark\b',
    r'\bwcag\b',
    r'\bapca\b'
]
INFERENCE_TOKENS = ['estimate', 'estimated', 'assumption', 'assume', 'inference', 'proxy', 'appears', 'likely', 'probably']
VISUAL_CLAIM_TOKENS = ['in the screenshot', 'in the mockup', 'i can see', 'the image shows', 'from the image']
VISUAL_BOUNDARY_TOKENS = ['observed', 'inferred', 'unverified', 'confidence', 'appears', 'likely', 'cannot verify from the image alone', 'visible evidence']
LOSS_TOKENS = ['sacrifice', 'lose', 'give up', 'cost', 'tradeoff', 'accept']
GAIN_TOKENS = ['preserve', 'gain', 'improve', 'unlock', 'protect', 'clarity']


def get_task(task_id: str) -> Dict:
    for task in CONTRACTS['tasks']:
        if task['task_id'] == task_id:
            return task
    raise KeyError(f'unknown task_id: {task_id}')


def tokenize(text: str) -> List[str]:
    return re.findall(r"[a-zA-Z0-9%:.#/+\-]+", text.lower())


def strip_session_state(text: str) -> str:
    """Remove [SESSION_STATE]...[/SESSION_STATE] metadata blocks before validation."""
    return re.sub(r'\[SESSION_STATE\].*?\[/SESSION_STATE\]', '', text, flags=re.DOTALL).strip()




def strip_markdown_headings(text: str) -> str:
    """Remove markdown and bold-only headings before evidence-class detection.

Evidence classes should be earned by recommendation content, not by a
contract heading such as "Verification checkpoints" or "Source constraints".
"""
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r'^#{1,6}\s+', stripped):
            continue
        if re.match(r'^\*\*[^*]+(?::)?\*\*\s*$', stripped):
            continue
        lines.append(line)
    return '\n'.join(lines)

def parse_sections(text: str) -> Dict[str, str]:
    text = strip_session_state(text)
    sections: Dict[str, List[str]] = {'_root': []}
    current = '_root'
    current_h2 = '_root'  # last h1/h2 heading -- sub-section content bubbles up here
    for line in text.splitlines():
        m = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if not m:
            # Also detect **Bold Header:** or **Bold Header** as section dividers
            m2 = re.match(r'^\*\*([^*]+?)(?::\*\*|\*\*)\s*$', line.strip())
            if m2:
                name = m2.group(1).strip().lower()
                current = name
                current_h2 = name  # treat bold headers as h2-level
                sections.setdefault(name, [])
                continue
        if m:
            level = len(m.group(1))
            name = m.group(2).strip().lower()
            if level <= 2:
                current_h2 = name
            current = name
            sections.setdefault(name, [])
        else:
            sections.setdefault(current, []).append(line)
            # Bubble sub-section content into parent h2 so word-count checks
            # succeed even when the model uses numbered sub-headings
            if current != current_h2 and current_h2 != '_root':
                sections.setdefault(current_h2, []).append(line)
    return {k: '\n'.join(v).strip() for k, v in sections.items()}


def section_word_count(text: str) -> int:
    return len([w for w in tokenize(text) if w not in STOPWORDS])


def information_density(text: str) -> float:
    words = tokenize(text)
    if not words:
        return 0.0
    content = [w for w in words if w not in STOPWORDS and len(w) > 2]
    if not content:
        return 0.0
    unique = len(set(content)) / len(content)
    substantive = len(content) / len(words)
    return round((unique + substantive) / 2, 3)


def prompt_overlap(prompt: str, output: str) -> float:
    p = {w for w in tokenize(prompt) if w not in STOPWORDS and len(w) > 2}
    o = {w for w in tokenize(output) if w not in STOPWORDS and len(w) > 2}
    if not p or not o:
        return 0.0
    return len(p & o) / max(1, len(p | o))


def evidence_count(text: str) -> int:
    return sum(len(re.findall(pat, text, flags=re.IGNORECASE)) for pats in EVIDENCE_CLASS_PATTERNS.values() for pat in pats)


def detected_evidence_classes(text: str, task: Dict = None) -> Set[str]:
    """Detect evidence classes in text.

    When a task is supplied, context_overrides from the task definition are
    checked in addition to global patterns. This lets domain-specific vocabulary
    (e.g. React state management terms) satisfy evidence classes whose global
    patterns were calibrated for a different domain (e.g. Next.js rendering).
    Context overrides are stored at the task level as:
      task.context_overrides = { class_id: [token, ...], ... }
    and also at the evidence class level as:
      required_evidence_classes[].context_overrides = { context_name: [token, ...] }
    Both forms are checked.
    """
    low = text.lower()
    found = set()
    for class_id, patterns in EVIDENCE_CLASS_PATTERNS.items():
        if any(re.search(p, low, flags=re.IGNORECASE) for p in patterns):
            found.add(class_id)
    if task:
        # Task-level context_overrides: { class_id: [token, ...] }
        task_overrides = task.get("context_overrides", {})
        for class_id, tokens in task_overrides.items():
            if class_id not in found:
                if any(tok.lower() in low for tok in tokens):
                    found.add(class_id)
        # Evidence-class-level context_overrides (legacy per-class form)
        for ev in task.get("required_evidence_classes", []):
            class_id = ev.get("class_id", "")
            overrides = ev.get("context_overrides", {})
            if class_id in found or not overrides:
                continue
            for _ctx_name, tokens in overrides.items():
                if any(tok.lower() in low for tok in tokens):
                    found.add(class_id)
                    break
    return found


# Decisions that are only required when the prompt contains relevant context signals.
# Format: { decision_id: [prompt_signal_tokens] }
# If NONE of the signal tokens appear in the prompt, the decision is skipped.
_CONDITIONAL_DECISIONS: Dict[str, List[str]] = {
    'async_job_model': [
        'async', 'background', 'long-running', 'queue', 'webhook',
        'job', 'polling', '202', 'event', 'stream', 'notify',
        'batch', 'deferred', 'processing', 'worker',
    ],
}


def find_missing_decisions(task: Dict, low: str, prompt_low: str = '') -> List[Dict]:
    missing = []
    for dec in task.get('required_decisions', []):
        if not isinstance(dec, dict):
            continue
        any_of = dec.get('any_of', [])
        # Skip decisions that have no detection tokens -- they are unverifiable by regex
        if not any_of:
            continue
        # Skip conditional decisions when the prompt does not signal the relevant context
        dec_id = dec.get('id', '')
        if dec_id in _CONDITIONAL_DECISIONS and prompt_low:
            signals = _CONDITIONAL_DECISIONS[dec_id]
            if not any(sig in prompt_low for sig in signals):
                continue  # prompt has no async signals — decision not applicable
        if not any(tok.lower() in low for tok in any_of):
            missing.append(dec)
    return missing


def find_missing_evidence_classes(task: Dict, classes_present: Set[str], output: str = '') -> List[Dict]:
    missing = []
    low = output.lower() if output else ''
    for ev in task.get('required_evidence_classes', []):
        ec_id = ev['class_id']
        if ec_id in classes_present:
            continue  # Layer 1: EVIDENCE_CLASS_PATTERNS match
        # Layer 2: token list match — check tokens directly in output
        # (_semantic_match was removed; it was never defined and token lists now cover all classes)
        if low:
            tokens = ev.get('tokens', [])
            if tokens and any(tok.lower() in low for tok in tokens):
                continue  # token match
        missing.append(ev)
    return missing


def has_route_traceability(low: str) -> bool:
    return (
        ('route:' in low and 'mode:' in low and 'phase:' in low) or
        ('<!-- route:' in low and '<!-- mode:' in low) or
        ('trace:' in low and 'route' in low)
    )


def unsupported_specificity(low: str, classes_present: Set[str]) -> bool:
    matches = sum(len(re.findall(pat, low, flags=re.IGNORECASE)) for pat in SPECIFICITY_PATTERNS)
    if matches == 0:
        return False
    if any(tok in low for tok in INFERENCE_TOKENS):
        return False
    if {'measurable_threshold', 'benchmark_artifact', 'standards_reference', 'file_backed_receipt'} & classes_present:
        return False
    return True


def route_bleed(task_id: str, low: str, missing_decisions: List[Dict]) -> bool:
    style_hits = sum(low.count(tok) for tok in STYLE_BLEED_TOKENS)
    if style_hits < 2:
        return False
    if task_id in {'backend_feasibility_review', 'pdf_remediation_plan', 'dashboard_audit', 'ui_structure_critique', 'case_study_rewrite'} and missing_decisions:
        return True
    return False


def unresolved_contradictions(low: str) -> List[str]:
    found = []
    for a, b in CONTRADICTION_PAIRS:
        if a in low and b in low and not any(tok in low for tok in GOVERNING_RULE_TOKENS):
            found.append(f'{a} / {b}')
    return found


def validate_load_state(pack_root: Path, route_id: str = '', task_id: str = '') -> Dict:
    statuses = []
    if not (pack_root / 'src' / 'operator' / 'core' / 'MASTER_CHAT_OPERATOR.md').exists():
        statuses.append({'class': 'below_minimum_viable_load', 'action': 'stop', 'detail': 'src/operator/core/MASTER_CHAT_OPERATOR.md missing'})
        return {'decision': 'FAIL', 'statuses': statuses}
    if not (pack_root / 'src' / 'schemas' / 'routing_registry.json').exists() or not (pack_root / 'src' / 'schemas' / 'task_contracts.json').exists():
        statuses.append({'class': 'below_minimum_viable_load', 'action': 'stop', 'detail': 'canonical routing or contract schema missing'})
        return {'decision': 'FAIL', 'statuses': statuses}
    if not (pack_root / 'src' / 'runtime' / 'boot' / 'core_bootstrap.md').exists() or not (pack_root / 'src' / 'runtime' / 'boot' / 'runtime_precedence.md').exists():
        statuses.append({'class': 'missing_boot_layer', 'action': 'continue_with_canonical', 'detail': 'runtime boot helper missing'})
    if route_id and not (pack_root / 'dist' / 'runtime' / 'routes' / f'{route_id}.json').exists():
        statuses.append({'class': 'missing_runtime_card_with_canonical_fallback', 'action': 'continue_with_canonical', 'detail': f'missing runtime route card {route_id}'})
    if task_id and not (pack_root / 'dist' / 'runtime' / 'contracts' / f'{task_id}.json').exists():
        statuses.append({'class': 'missing_runtime_card_with_canonical_fallback', 'action': 'continue_with_canonical', 'detail': f'missing runtime contract card {task_id}'})
    if not (pack_root / 'src' / 'operator' / 'core' / 'SESSION_CONTEXT.md').exists():
        if (pack_root / 'src' / 'operator' / 'core' / 'SESSION_CONTEXT_DEFAULTS.md').exists():
            statuses.append({'class': 'missing_session_state', 'action': 'continue_with_defaults', 'detail': 'src/operator/core/SESSION_CONTEXT.md missing; defaults available'})
        else:
            statuses.append({'class': 'below_minimum_viable_load', 'action': 'stop', 'detail': 'src/operator/core/SESSION_CONTEXT.md missing and defaults unavailable'})
    decision = 'FAIL' if any(s['class'] == 'below_minimum_viable_load' for s in statuses) else 'PASS'
    return {'decision': decision, 'statuses': statuses}


def validate_runtime_overlay_assets(pack_root: Path) -> Dict:
    errors, warnings = [], []
    contracts = json.loads((pack_root / 'src' / 'schemas' / 'task_contracts.json').read_text(encoding='utf-8'))
    routes = json.loads((pack_root / 'src' / 'schemas' / 'routing_registry.json').read_text(encoding='utf-8'))
    task_ids = {t['task_id'] for t in contracts['tasks']}
    route_ids = {r['route_id'] for r in routes['routes']}

    load_report = validate_load_state(pack_root)
    for status in load_report['statuses']:
        if status['action'] == 'stop':
            errors.append(status['detail'])
        else:
            warnings.append(status['detail'])

    for route in route_ids:
        if not (pack_root / 'dist' / 'runtime' / 'routes' / f'{route}.json').exists():
            errors.append(f'missing runtime route card: {route}')
    for task in task_ids:
        if not (pack_root / 'dist' / 'runtime' / 'contracts' / f'{task}.json').exists():
            errors.append(f'missing runtime contract card: {task}')

    for rel in ['src/operator/protocols/DEGRADED_MODE_PROTOCOL.md', 'src/operator/protocols/VISUAL_INPUT_PROTOCOL.md', 'src/operator/protocols/LIGHTWEIGHT_RESPONSE_PROTOCOL.md', 'QUICKSTART.md']:
        if not (pack_root / rel).exists():
            errors.append(f'{rel} missing')

    control_map = (pack_root / 'src' / 'operator' / 'governance' / 'CONTROL_AUTHORITY_MAP.md').read_text(encoding='utf-8').lower()
    if ('human-readable mirrors - maintenance/debug only' not in control_map
            and 'human-readable mirrors — maintenance/debug only' not in control_map):
        errors.append('maintenance docs are not demoted in control authority map')
    if 'startup authority: `master_chat_operator.md`' not in control_map:
        errors.append('single startup authority not declared in control authority map')

    return {
        'check': 'capability_preservation_validation',
        'decision': 'PASS' if not errors else 'FAIL',
        'errors': errors,
        'warnings': warnings,
        'load_state': load_report
    }


def content_tokens(text: str) -> Set[str]:
    return {w for w in tokenize(text) if w not in STOPWORDS and len(w) > 3}




def prompt_has_visual(prompt: str) -> bool:
    # Only fire when the model is being asked to ANALYZE an attached image/screenshot,
    # not when the prompt merely describes an image that exists on a page.
    low = prompt.lower()
    return any(tok in low for tok in [
        'screenshot', 'mockup', 'page image', 'from a screenshot',
        'image shows', 'image attached', 'attached image', 'uploaded image',
        'this image', 'this screenshot', 'this mockup', 'the screenshot',
        'look at the', 'analyze this image', 'review this image',
    ])

def lightweight_class(task: Dict, prompt: str) -> str:
    low = prompt.lower()
    if task.get('task_weight_default') == 'compound':
        return 'compound'
    if task.get('task_weight_default') == 'lightweight':
        return 'lightweight'
    quick_tokens = ['quick', 'brief', 'one sentence', 'tight', 'short', 'just fix', 'small rewrite']
    if any(tok in low for tok in quick_tokens) and len(tokenize(prompt)) < 40 and task.get('supports_lightweight_response', True):
        return 'lightweight'
    if any(tok in low for tok in ['architecture', 'proof', 'semantics', 'multi-tenant', 'api', 'pdf', 'contract']):
        return 'compound'
    return task.get('task_weight_default', 'standard')


def fake_tradeoff(low: str) -> bool:
    if not any(tok in low for tok in ['tradeoff', 'trade-off']):
        return False
    return not any(tok in low for tok in LOSS_TOKENS) and not any(tok in low for tok in GAIN_TOKENS)


def recommendation_alignment_problem(sections: Dict[str, str]) -> bool:
    # Order-agnostic cross-model vocabulary for finding and recommendation sections
    FINDING_KEYS = {
        'finding', 'key failures', 'problem framing', 'dashboard role',
        'source constraints', 'initial assessment', 'audit results',
        'diagnostic summary', 'evidence synthesis', 'identified issues',
        'logic discrepancies', 'the problem', "what's wrong", 'identified problems',
        'key deficiencies', 'critique findings', 'error localization',
    }
    REC_KEYS = {
        'recommend', 'rebuild path', 'rebuild sequence', 'recommendations',
        'remediation strategy', 'actionable moves', 'strategic interventions',
        'proposed changes', 'fix steps', 'suggested moves', 'proposed patches',
        'fix list', 'action plan', 'intervention order', 'intervention steps',
        'first-response actions', 'suggested fixes', 'repair sequence',
    }
    findings = ''
    recs = ''
    for name, content in sections.items():
        lname = name.lower()
        if any(k in lname for k in FINDING_KEYS):
            findings += ' ' + content
        if any(k in lname for k in REC_KEYS):
            recs += ' ' + content
    ft, rt = content_tokens(findings), content_tokens(recs)
    if len(ft) < 8 or len(rt) < 8:
        return False
    return len(ft & rt) < 2


def visual_boundary_problem(task_id: str, prompt: str, low: str) -> bool:
    if task_id not in {'ui_structure_critique', 'dashboard_audit', 'layout_reconstruction_plan', 'pdf_remediation_plan', 'graphic_critique', 'accessibility_feedback_audit'}:
        return False
    if not prompt_has_visual(prompt):
        return False
    if not any(tok in low for tok in VISUAL_CLAIM_TOKENS):
        return False
    return not any(tok in low for tok in VISUAL_BOUNDARY_TOKENS)


def visible_trace_expected(low: str) -> bool:
    return any(tok in low for tok in ['validator report', 'debug', 'maintenance', 'audit log', 'trace requested'])


NEGATION_WINDOW = 80  # chars before pattern to scan for negation prefix
NEGATION_PREFIXES = re.compile(
    # Matches negation words at the end of the before-window.
    # Allows up to 25 chars of intervening words/markdown after the negation.
    # "do **not** flatten", "do not simply flatten", "**avoid**: flatten"
    r"\b(do not|don't|never|avoid|must not|should not|not to|without"  # core
    r"|rejected|reject|prohibited|forbidden|warning|caution"  # explicit rejection labels
    r")\b.{0,25}$",
    re.IGNORECASE | re.DOTALL,
)


def positively_present(text: str, pattern: str) -> bool:
    """True if `pattern` appears in `text` WITHOUT an immediately preceding negation.

    Strips markdown bold/italic markers before checking so that "do **not** flatten"
    is correctly identified as negated. Checks a window of NEGATION_WINDOW chars before
    each occurrence.
    """
    pat_lower = pattern.lower()
    start = 0
    while True:
        idx = text.find(pat_lower, start)
        if idx == -1:
            return False
        before = text[max(0, idx - NEGATION_WINDOW):idx]
        # Strip markdown bold/italic markers so "**not**" matches as "not"
        # Strip markdown and normalize whitespace so 'do **not**' → 'do not'
        before_clean = re.sub(r'\s+', ' ', re.sub(r'[*_]+', ' ', before)).strip()
        if not NEGATION_PREFIXES.search(before_clean):
            return True  # found at least one non-negated occurrence
        start = idx + 1


# Semantic aliases for required section names -- loaded from src/schemas/section_aliases.json
# Edit that file to add new aliases; do not hardcode them here.
SECTION_ALIASES: dict[str, list[str]] = json.loads(
    (ROOT / 'src' / 'schemas' / 'section_aliases.json').read_text(encoding='utf-8')
)['aliases']


def _section_alias_match(required_name: str, sections: dict) -> str | None:
    """Return section content if any alias for `required_name` matches a key in `sections`."""
    aliases = SECTION_ALIASES.get(required_name.lower(), [])
    for alias in aliases:
        for sec_name, content in sections.items():
            if alias in sec_name or sec_name in alias:
                return content
    # Special case: for "Revised passage" check root content for revision signals
    if required_name.lower() == 'revised passage':
        root = sections.get('_root', '')
        revision_signals = ["here's the revised", "here is the revised", "revised paragraph",
                            "revised version", "revised text", "rewritten paragraph",
                            "here’s the revised"]
        if any(sig in root.lower() for sig in revision_signals):
            # Root contains the revision inline — treat it as present
            return root or ' '
        # Also check if any section key looks like actual revised content (short, bold-was-revision)
        # Any section with > 5 words that comes before 'what changed' is likely the revision
        sec_items = [(k, v) for k, v in sections.items() if k != '_root']
        if sec_items:
            first_sec_name, first_sec_content = sec_items[0]
            if 'what changed' in ''.join(k for k,_ in sec_items[1:]) or 'why' in ''.join(k for k,_ in sec_items[1:]):
                # First section is likely the revision if followed by explanation
                return first_sec_content or ' '
    return None


def _has_structural_tradeoff(low: str) -> bool:
    """Detect tradeoff by structure (comparison + cost/benefit) not just vocabulary."""
    # Strong signals: explicit comparison operators
    comparison_signals = [
        r'\bvs\.?\b', r'\bversus\b', r'\binstead of\b', r'\brather than\b',
        r'\b(option|path|approach|pattern|method)\s+(a|b|1|2)\b',
        r'\bchoose\b.{0,40}\b(over|instead|rather)\b',
        r'\b(a|b):\s',
        # Cross-model additions (xAI, DeepSeek, OpenAI vocabulary)
        r'\bthe cost of\b', r'\bthe cost is\b', r'\bat the cost\b',
        r'\bthe risk here\b', r'\bthe tradeoff here\b',
        r'\bone downside\b', r'\bthe downside of\b',
        r'\bthis means accepting\b', r'\bmeans giving up\b',
        r'\byou lose\b', r'\byou gain\b',
        r'\bwhat you give up\b', r'\bwhat you get\b',
        r'\bweigh(s|ing)?\b.{0,30}\b(against|vs)\b',
        r'\bon the other hand\b', r'\bpros and cons\b',
        r'\bthe catch is\b', r'\bthe gotcha\b',
        r'\bat the expense of\b', r'\byou sacrifice\b',
    ]
    loss_patterns = [r'\bcost\b', r'\bdownside\b', r'\bsacrifice\b',
                     r'\blose\b', r'\bgive up\b', r'\btax\b', r'\btradeoff\b']
    gain_patterns = [r'\bgain\b', r'\bpreserve\b', r'\bbenefit\b',
                     r'\bunlock\b', r'\bprotect\b', r'\bimprove\b', r'\bwin\b']

    for pat in comparison_signals:
        if re.search(pat, low):
            return True
    has_loss = any(re.search(p, low) for p in loss_patterns)
    has_gain = any(re.search(p, low) for p in gain_patterns)
    if has_loss and has_gain:
        return True
    # Fallback: existing token list
    return any(tok.strip() in low for tok in TRADEOFF_TOKENS)


def _has_structural_rationale(low: str) -> bool:
    """Detect rationale by causal structure not just vocabulary."""
    causal_patterns = [
        r'\bbecause\b', r'\btherefore\b', r'\bso that\b', r'\bsince\b',
        r'\bgiven that\b', r'\bwhich means\b', r'\bthis means\b',
        r'\bas a result\b', r'\bconsequently\b', r'\bthe reason\b',
        r'\bwhy\b.{0,20}\b(this|we|it|the)\b', r'\bin order to\b',
        r'\bto ensure\b', r'\bto prevent\b', r'\bwithout this\b',
        r'\bif not\b', r'\botherwise\b',
        # Cross-model additions (xAI, DeepSeek, OpenAI vocabulary)
        r'\bthe reasoning\b', r'\bmy reasoning\b',
        r'\bthe reason to\b', r'\bthe reason for\b',
        r'\bthis is important\b', r'\bthis matters\b',
        r'\bthis is necessary\b', r'\bthis is required\b',
        r'\bby doing so\b', r'\bin doing so\b',
        r'\bthis allows\b', r'\bthis enables\b', r'\bthis forces\b',
        r'\bwithout which\b', r'\bfailing to\b',
        r'\bthe implication\b', r'\bthe consequence\b',
        r'\bthis choice\b', r'\bthis decision\b',
        r'\bthis approach\b.{0,30}\b(ensures|prevents|forces|allows)\b',
    ]
    consequence_patterns = [
        r'\b(this|it) (breaks|fails|creates|causes|prevents|ensures|fixes)\b',
        r'\b(this|it) (means|results in|leads to)\b',
        r'\bwould (break|fail|cause|prevent|ensure)\b',
    ]
    for pat in causal_patterns + consequence_patterns:
        if re.search(pat, low):
            return True
    # Fallback: existing token list
    return any(tok in low for tok in RATIONALE_TOKENS)


def _has_attached_rationale(text: str) -> bool:
    """Check that causal language appears within 120 words of a recommendation signal.

    This is stronger than _has_structural_rationale() which just checks anywhere in
    the text. Models can satisfy the global check with "because" in a preamble while
    providing bare recommendations with no causal grounding.

    Returns True if at least one recommendation-adjacent causal phrase is found.
    Falls back gracefully — if no recommendation signals found, returns True to avoid
    false positives on non-recommendation tasks.
    """
    RECOMMENDATION_SIGNALS = [
        r'\brecommend\b', r'\bshould\b', r'\bmust\b', r'\bavoid\b',
        r'\buse .{0,20} instead\b', r'\bswitch to\b', r'\breplace\b',
        r'\bprioritize\b', r'\bfirst[,:]\b', r'\bstep \d\b',
    ]
    CAUSAL_NEAR = [
        r'\bbecause\b', r'\bwithout which\b', r'\bthis requires\b',
        r'\bthe constraint\b', r'\bby doing so\b', r'\bif you skip\b',
        r'\bthe reason\b', r'\bthis enables\b', r'\bthis prevents\b',
        r'\bthis allows\b', r'\bthis forces\b', r'\bfailing to\b',
        r'\bthe implication\b', r'\bthe consequence\b',
        r'\btherefore\b', r'\bso that\b', r'\bas a result\b',
        # Tradeoff framing — Claude uses "Tradeoff: you sacrifice X to gain Y"
        r'\btradeoff\b', r'\byou sacrifice\b', r'\byou accept\b',
        r'\bthe cost\b', r'\bthe downside\b', r'\bat the cost\b',
        # Explanation-of-change framing — used by text_humanization and case study tasks
        r'\bwhat changed\b', r'\bwhy this\b', r'\bwhy it\b',
        r'\bcut the\b', r'\breplaced\b', r'\bswapped\b', r'\bremoved\b',
        r'\binstead of\b', r'\brather than\b', r'\bover\b.{0,15}\bwhich\b',
        r'\bthis removes\b', r'\bthis adds\b', r'\bthis keeps\b',
        r'\bthis cuts\b', r'\bthis replaces\b', r'\bthis clears\b',
        r'\bmore direct\b', r'\bclearer\b.{0,20}\bbecause\b',
        r'\bstronger\b.{0,20}\bverb\b', r'\bactive\b.{0,20}\bpassive\b',
    ]
    words = text.split()
    rec_positions = []
    for i, _ in enumerate(words):
        chunk = ' '.join(words[max(0, i-2):i+3])
        if any(re.search(p, chunk, re.IGNORECASE) for p in RECOMMENDATION_SIGNALS):
            rec_positions.append(i)

    if not rec_positions:
        return True  # No recommendation signals found — not a recommendation task, don't penalise

    # Check if any causal phrase appears within the window of any recommendation.
    # Window is asymmetric: 80 words BEFORE and 90 words AFTER the recommendation signal.
    # The wider backward window catches "because X, you should do Y" patterns where
    # causal language precedes the recommendation (common in Claude outputs).
    for rec_pos in rec_positions:
        window_start = max(0, rec_pos - 120)
        window_end = min(len(words), rec_pos + 120)
        window = ' '.join(words[window_start:window_end])
        if any(re.search(p, window, re.IGNORECASE) for p in CAUSAL_NEAR):
            return True  # Found causal language near at least one recommendation

    return False


# ── CROSS-MODEL PREPROCESSING ─────────────────────────────────────────────

def strip_reasoning_blocks(text: str) -> str:
    """Remove chain-of-thought reasoning blocks and routing preambles before validation.

    Handles:
    - DeepSeek-R1 / Qwen thinking mode: <think>...</think> or <thinking>...</thinking>
    - Magistral: blockquote preambles (> ...) before the first heading
    - OpenAI o-series: if reasoning_content was accidentally concatenated
    - Gemini / Claude routing metadata: 'Mode: X | Phase: Y | Route: Z' lines
      that appear when the system prompt instructs models to emit route metadata
    """
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<thinking>.*?</thinking>', '', text, flags=re.DOTALL | re.IGNORECASE)

    # Strip routing metadata lines: "Mode: STANDARD | Phase: X | Route: Y"
    # These appear when models follow the system-prompt instruction to emit route context.
    # They inflate apparent section count and consume early token budget in Gemini.
    text = re.sub(
        r'\*?\s*Mode:\s*\S+.*?Route:\s*[A-Za-z_]+\*?\s*\n?',
        '',
        text,
        flags=re.IGNORECASE,
    )

    # Strip routing/metadata preamble blocks before the first real heading.
    # Fires when a model emits 2+ lines of "Governing Route:", "Task Weight:",
    # "Active Skills:" etc. before starting the actual analytical content.
    first_heading = re.search(r'^#{1,3}\s', text, re.MULTILINE)
    if first_heading:
        preamble = text[:first_heading.start()]
        preamble_lines = preamble.splitlines()
        ROUTING_INDICATORS = [
            'governing route', 'task weight', 'active skills',
            'skills:', 'route:', 'phase:', 'mode:', 'supporting skills',
        ]
        routing_line_count = sum(
            1 for ln in preamble_lines
            if any(ind in ln.lower() for ind in ROUTING_INDICATORS)
        )
        if routing_line_count >= 2:
            text = text[first_heading.start():]

    # Strip Magistral-style blockquote reasoning preambles
    first_heading = re.search(r'^#{1,3}\s', text, re.MULTILINE)
    if first_heading:
        preamble = text[:first_heading.start()]
        lines = [l for l in preamble.splitlines() if l.strip()]
        if lines:
            blockquote_ratio = sum(1 for l in lines if l.strip().startswith('>')) / len(lines)
            if blockquote_ratio > 0.6:
                text = text[first_heading.start():]

    return text.strip()


def strip_deductive_preamble(text: str) -> str:
    """Strip executive summary preambles used by deductive models (GPT-5.4, Llama 4 Maverick).

    These models open with a summary block before the detailed analysis. This block
    overlaps heavily with the prompt by design. Stripping it prevents false
    prompt_restatement failures on outputs that are substantively correct.
    """
    PREAMBLE_HEADINGS = {
        'executive summary', 'summary', 'overview', 'bottom line',
        'tl;dr', 'tldr', 'key takeaways', 'in brief', 'at a glance',
        'initial assessment', 'goal summary', 'task overview',
    }
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r'^#{1,3}\s+(.+)$', line.strip())
        if m:
            heading = m.group(1).strip().lower()
            if heading in PREAMBLE_HEADINGS:
                for j in range(i + 1, len(lines)):
                    if re.match(r'^#{1,3}\s+', lines[j].strip()):
                        return '\n'.join(lines[j:])
    return text


def effective_min_density(task: Dict, output: str) -> float:
    """Return the appropriate density floor based on output length characteristics.

    Compact models (o4-mini, Mistral Small 4, Llama 4 Scout) are documented to
    produce correct but concise outputs. The standard 0.42 threshold was calibrated
    on Sonnet-class outputs and produces false negatives for compact models.
    Threshold is reduced to 0.35 when total content is under 130% of the word minimum.
    """
    base = task.get('min_density', 0.42)
    content_words = section_word_count(output)
    min_words = sum(sec.get('min_words', 0) for sec in task.get('required_sections', []))
    if content_words < int(min_words * 1.3):
        return min(base, 0.35)
    return base


def likely_truncated(output: str) -> bool:
    """Heuristic check for mid-generation truncation (DeepSeek-V3, early Gemini).

    Fires when output ends without a sentence-ending character, or with an
    unclosed code block, suggesting the model was cut off mid-generation.
    """
    stripped = output.strip()
    if not stripped or len(stripped) < 100:
        return False
    last_50 = stripped[-50:]
    signals = [
        not re.search(r'[.!?)\]`]$', last_50),
        stripped.count('```') % 2 != 0,
        stripped.endswith('...') and len(stripped) > 500,
    ]
    return sum(signals) >= 2


# Map from required section names to evidence classes whose presence in content
# confirms the section topic — used as fallback 3b in section matching.
SECTION_EVIDENCE_CLASS_MAP = {
    'rendering and mutation strategy': ['rendering_boundary_rule'],
    'risks and safer path': ['implementation_constraint'],
    'resilience and observability': ['resilience_rule'],
    'source constraints': ['implementation_constraint', 'verification_method'],
    'feasibility assessment': ['implementation_constraint'],
    'authorization and resource protection': ['permission_rule'],
    'idempotency and async lifecycle': ['async_lifecycle_rule', 'consistency_model'],
    'failure semantics': ['failure_semantics_rule'],
    'outcome and proof': ['narrative_proof_boundary', 'file_backed_receipt'],
    'trust and proof burden': ['implementation_constraint', 'file_backed_receipt'],
}


def _section_evidence_match(required_name: str, sections: Dict, task: Dict = None) -> str | None:
    """Match a required section by evidence class presence in section content.

    If any actual section's content triggers an evidence class associated with
    the required section, treat that section as satisfying the requirement.
    Picks the longest matching section to avoid matching thin stub sections.
    """
    target_classes = SECTION_EVIDENCE_CLASS_MAP.get(required_name.lower())
    if not target_classes:
        return None
    best_content = None
    best_word_count = 0
    for sec_name, content in sections.items():
        if sec_name == '_root' or not content.strip():
            continue
        classes_in_section = detected_evidence_classes(content, task=task)
        if any(cls in classes_in_section for cls in target_classes):
            wc = section_word_count(content)
            if wc > best_word_count:
                best_word_count = wc
                best_content = content
    return best_content if best_word_count >= 10 else None


def _section_covered_in_body(required_name: str, req_rationale: str, output_low: str) -> bool:
    """True if the required section's topic appears somewhere in the full output body.

    Used to distinguish vocabulary-mismatch failures (content present, heading wrong)
    from genuine structural omissions (topic not covered at all).
    Requires at least 2 overlapping non-stopword words between the rationale description
    and the output body.
    """
    if not req_rationale:
        return False
    # Use tokenize() on both sides so punctuation never prevents a match
    # (old: .split() kept "barriers," which never matched "barriers")
    rationale_words = set(tokenize(req_rationale.lower())) - STOPWORDS
    content_words = set(tokenize(output_low)) - STOPWORDS
    return len(rationale_words & content_words) >= 2


def validate_output(task_id: str, prompt: str, output: str, project_root: str = '', model_hint: str = '') -> Dict:
    task = get_task(task_id)
    # ── Preprocessing: strip reasoning blocks (DeepSeek/Qwen/Magistral) ──
    output = strip_reasoning_blocks(output)
    issues = []
    warnings = []
    sections = parse_sections(output)
    density = information_density(output)
    # Use deductive-preamble-stripped version for overlap — prevents false
    # prompt_restatement failures on GPT-5.4 / Llama 4 Maverick executive summaries
    overlap = prompt_overlap(prompt, strip_deductive_preamble(output))
    evidence = evidence_count(output)
    total_content_words = section_word_count(output)
    weight = lightweight_class(task, prompt)
    min_total_words = sum(sec['min_words'] for sec in task['required_sections'])
    if weight == 'lightweight':
        min_total_words = int(min_total_words * 0.7)
    score = 100
    low = output.lower()
    evidence_body = strip_markdown_headings(output)
    classes_present = detected_evidence_classes(evidence_body, task=task)
    _model_hint = model_hint  # available for downstream result reporting

    for phrase in PLACEHOLDER_PHRASES:
        # Use word-boundary check for short tokens like 'tbd' to avoid
        # false positives on substrings (e.g. 'jtbd' = Jobs To Be Done)
        if phrase in ('tbd', 'lorem ipsum'):
            import re as _re
            matched = bool(_re.search(r'\\b' + _re.escape(phrase) + r'\\b', low))
        else:
            matched = phrase in low
        if matched:
            issues.append({'id': 'placeholder_text', 'severity': 'hard', 'detail': f'placeholder phrase present: {phrase}'})
            score -= 20

    for req in task['required_sections']:
        heading = req['name'].lower()
        # Primary: exact substring match. Fallback: first significant word match
        # (handles model using "Phase 5: Verification and export" for "Verification checks")
        heading_words = [w for w in heading.split() if len(w) > 4]
        match = None
        for sec_name, content in sections.items():
            if heading in sec_name:
                match = content
                break
        if match is None and heading_words:
            # Fallback 2: word-prefix match ("safer" matches "safe path forward")
            heading_stems = [w[:5] for w in heading_words if len(w) >= 5]
            for sec_name, content in sections.items():
                sec_words = sec_name.split()
                if any(sw.startswith(stem) for stem in heading_stems for sw in sec_words):
                    match = content
                    break
        if match is None:
            # Fallback 3: semantic alias match ("key failures" accepted for "Findings")
            match = _section_alias_match(req['name'], sections)
        if match is None:
            # Fallback 3b: evidence-class presence in section content
            # Catches "Strategic tier" satisfying "Risks and safer path" when the
            # content triggers implementation_constraint evidence class
            match = _section_evidence_match(req['name'], sections, task=task)
        if match is None:
            # Fallback 4: keyword overlap with section rationale
            # "Migration notes -- Shows how to move from the current palette safely" is satisfied
            # by any section whose content overlaps meaningfully with that rationale description.
            req_rationale = req.get('rationale', '') if isinstance(req, dict) else ''
            if req_rationale:
                # Use tokenize() so punctuation in rationale strings never blocks a match
                rationale_words = set(tokenize(req_rationale.lower())) - STOPWORDS
                best_score = 0
                best_content = None
                for sec_name, content in sections.items():
                    if sec_name == '_root':
                        continue
                    sec_words = set(tokenize(content)) - STOPWORDS
                    overlap = len(rationale_words & sec_words)
                    min_w = int(req.get('min_words', 10) * 0.5) if isinstance(req, dict) else 5
                    if overlap > best_score and section_word_count(content) >= min_w:
                        best_score = overlap
                        best_content = content
                if best_score >= 2:  # Lowered from 3 — catches tier-framed content
                    match = best_content
        if match is None:
            # Fallback 5: _root content -- model put deliverable before first heading
            root_content = sections.get('_root', '').strip()
            if root_content and section_word_count(root_content) >= int(req.get('min_words', 10) * 0.6):
                match = root_content
        if match is None:
            # Distinguish vocabulary mismatch (content exists, heading differs) from
            # genuine structural omission (topic not covered anywhere in output)
            req_rationale = req.get('rationale', '') if isinstance(req, dict) else ''
            covered_in_body = _section_covered_in_body(req['name'], req_rationale, low)
            if covered_in_body:
                # Content present somewhere but heading doesn't match — vocabulary mismatch
                warnings.append({
                    'id': 'missing_section_heading',
                    'severity': 'soft',
                    'detail': f'section content for "{req["name"]}" appears present but heading does not match contract vocabulary'
                })
                score -= 6
            else:
                # Genuine structural omission — topic not covered at all
                issues.append({'id': 'missing_section', 'severity': 'hard', 'detail': f'missing section: {req["name"]}'})
                score -= 12
        else:
            count = section_word_count(match)
            required_words = int(req['min_words'] * (0.75 if weight == 'lightweight' else 1.0))
            if count < required_words:
                # Section exists but is under the word target — soft warning, not hard failure.
                # Structure is present; detail is lacking. Produces AUTO_REVISE not FAIL.
                warnings.append({'id': 'thin_section', 'severity': 'soft', 'detail': f'section {req["name"]} too thin: {count} < {required_words}'})
                score -= 6

    # Use model-size-aware density floor (0.35 for compact models, 0.42 for standard)
    effective_density_floor = effective_min_density(task, output)
    if density < effective_density_floor or total_content_words < int(min_total_words * 0.7):
        issues.append({'id': 'low_information_density', 'severity': 'hard', 'detail': f'density {density} / content words {total_content_words} below expected depth {int(min_total_words * 0.7)} (floor={effective_density_floor})'})
        score -= 12
    if (overlap > 0.55 and len(tokenize(output)) < 220) or (overlap > 0.25 and total_content_words < int(min_total_words * 0.9)):
        issues.append({'id': 'prompt_restatement', 'severity': 'hard', 'detail': f'prompt overlap too high for the amount of transformation: {overlap:.2f}'})
        score -= 12

    required_evidence = max(1, task['required_evidence_count'] - (1 if weight == 'lightweight' else 0))
    if evidence < required_evidence:
        issues.append({'id': 'insufficient_evidence', 'severity': 'hard', 'detail': f'evidence count {evidence} below required {required_evidence}'})
        score -= 12
    if task.get('require_tradeoff') and not _has_structural_tradeoff(low):
        issues.append({'id': 'missing_tradeoff', 'severity': 'hard', 'detail': 'no explicit tradeoff language found'})
        score -= 10
    if fake_tradeoff(low):
        issues.append({'id': 'fake_tradeoff', 'severity': 'hard', 'detail': 'tradeoff language is present without both gain and sacrifice'})
        score -= 10
    if task.get('require_rationale') and not _has_structural_rationale(low):
        issues.append({'id': 'missing_rationale', 'severity': 'hard', 'detail': 'no explicit rationale language found'})
        score -= 10
    elif task.get('require_rationale') and not _has_attached_rationale(output):
        issues.append({'id': 'missing_rationale', 'severity': 'soft',
                       'detail': 'causal language not attached near recommendations — add "because/without which/this requires" adjacent to each recommendation'})
        score -= 4
    if task.get('require_alternatives') and not any(tok in low for tok in ALTERNATIVE_TOKENS):
        warnings.append({'id': 'missing_alternative', 'severity': 'soft', 'detail': 'no alternative path was named'})
        score -= 4

    if ('functional' in low or 'integrative' in low) and not any(tok in low for tok in ['next step', 'start with', 'first move', 'safer next move', 'then']):
        warnings.append({'id': 'missing_next_step_guidance', 'severity': 'soft', 'detail': 'designer-readable guidance is missing a visible next move'})
        score -= 4

    if task_id == 'text_humanization_revision' and 'meaning_preservation_guard' not in classes_present:
        issues.append({'id': 'missing_meaning_guard', 'severity': 'hard', 'detail': 'text humanization requires a visible meaning-preservation guard'})
        score -= 10

    visual_prompt = prompt_has_visual(prompt)
    raw_missing_decisions = find_missing_decisions(task, low, prompt_low=prompt.lower())
    missing_decisions = []
    for dec in raw_missing_decisions:
        if dec.get('id') == 'visual_confidence_boundary' and not visual_prompt:
            continue
        missing_decisions.append(dec)
    for dec in missing_decisions:
        issues.append({'id': 'missing_required_decision', 'severity': 'hard', 'detail': f"missing required decision `{dec['id']}`: {dec['description']}"})
        score -= 8

    raw_missing_classes = find_missing_evidence_classes(task, classes_present, evidence_body)
    missing_classes = []
    for ev in raw_missing_classes:
        if ev.get('class_id') == 'visual_structure_rule' and not visual_prompt:
            continue
        missing_classes.append(ev)
    for ev in missing_classes:
        issues.append({'id': 'missing_evidence_class', 'severity': 'hard', 'detail': f"missing evidence class `{ev['class_id']}`: {ev['description']}"})
        score -= 8

    for item in task.get('forbidden_shortcuts', []):
        if any(positively_present(low, p) for p in item.get('patterns', [])):
            issues.append({'id': 'forbidden_shortcut', 'severity': 'hard', 'detail': f"forbidden shortcut `{item['id']}` triggered"})
            score -= 10

    for item in task.get('overclaim_rules', []):
        forbidden_hit = [term for term in item.get('forbidden_terms', []) if term.lower() in low]
        if forbidden_hit and not any(term.lower() in low for term in item.get('allowed_if_any', [])):
            issues.append({'id': 'overclaim_without_evidence', 'severity': 'hard', 'detail': f"overclaim rule `{item['id']}` triggered by: {', '.join(forbidden_hit)}"})
            score -= 10

    for word in SUPERLATIVES:
        # Use word-boundary match to avoid false positives (e.g. 'validated' in 'invalidated')
        if re.search(r'\b' + re.escape(word) + r'\b', low) and not ({'measurable_threshold', 'benchmark_artifact', 'file_backed_receipt', 'reviewer_confidence_artifact'} & classes_present):
            issues.append({'id': 'unsupported_superlative', 'severity': 'hard', 'detail': f'{word} used without the required proof class'})
            score -= 10

    if not task.get('specificity_exempt') and unsupported_specificity(low, classes_present):
        issues.append({'id': 'unsupported_specificity', 'severity': 'hard', 'detail': 'precise-seeming thresholds or scores were introduced without a standard, artifact, or inference label'})
        score -= 10

    if route_bleed(task_id, low, missing_decisions):
        issues.append({'id': 'route_bleed', 'severity': 'hard', 'detail': 'adjacent-domain styling language is present while governing route decisions are still missing'})
        score -= 10

    contradictions = unresolved_contradictions(low)
    for c in contradictions:
        issues.append({'id': 'contradiction', 'severity': 'hard', 'detail': f'unresolved contradiction: {c}'})
        score -= 10

    if recommendation_alignment_problem(sections):
        issues.append({'id': 'hollow_compliance', 'severity': 'hard', 'detail': 'recommendations do not map back to named findings strongly enough'})
        score -= 10

    if visual_boundary_problem(task_id, prompt, low):
        issues.append({'id': 'overconfident_visual_claim', 'severity': 'hard', 'detail': 'visual claims are presented without an observed vs inferred boundary'})
        score -= 10

    for pat in task.get('hard_fail_patterns', []):
        if positively_present(low, pat):
            issues.append({'id': 'hard_fail_pattern', 'severity': 'hard', 'detail': f'forbidden hard-fail pattern present: {pat}'})
            score -= 12
    for pat in task.get('soft_fail_patterns', []):
        if pat.lower() in low:
            warnings.append({'id': 'soft_fail_pattern', 'severity': 'soft', 'detail': f'soft-fail pattern present: {pat}'})
            score -= 4

    if visible_trace_expected(low) and not has_route_traceability(low):
        warnings.append({'id': 'missing_route_traceability', 'severity': 'soft', 'detail': 'visible trace was expected but route metadata is not recoverable enough for debugging'})
        score -= 3

    decision = 'PASS'
    if any(i['severity'] == 'hard' for i in issues):
        decision = 'FAIL'
    elif warnings:
        decision = 'AUTO_REVISE'
    # Truncation detection (DeepSeek-V3, early Gemini mid-generation cut-offs)
    if likely_truncated(output):
        warnings.append({'id': 'likely_truncated', 'severity': 'soft',
                         'detail': 'output appears to end mid-generation; later sections may be incomplete'})
        score -= 8
        if decision != 'FAIL':
            decision = 'AUTO_REVISE'

    return {
        'task_id': task_id,
        'task_weight': weight,
        'density': density,
        'density_floor_used': effective_density_floor if 'effective_density_floor' in dir() else task.get('min_density', 0.42),
        'prompt_overlap': round(overlap, 3),
        'evidence_count': evidence,
        'evidence_classes_present': sorted(classes_present),
        'issues': issues,
        'warnings': warnings,
        'score': max(0, score),
        'decision': decision,
        'model_hint': _model_hint,
        'checked_rules': [r['rule_id'] for cat in ('hard_rules', 'semantic_rules', 'integrity_rules') for r in RULES.get(cat, [])]
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', required=False)
    parser.add_argument('--prompt', default='')
    parser.add_argument('--prompt-file')
    parser.add_argument('--file')
    parser.add_argument('--project-root', default='')
    parser.add_argument('--validate-runtime-overlay', action='store_true')
    parser.add_argument('--check-load-state', action='store_true')
    parser.add_argument('--route-id', default='')
    args = parser.parse_args()

    pack_root = Path(args.project_root) if args.project_root else ROOT

    if args.check_load_state:
        report = validate_load_state(pack_root, args.route_id, args.task or '')
        print(json.dumps(report, indent=2))
        if report['decision'] == 'FAIL':
            raise SystemExit(1)
        return

    if args.validate_runtime_overlay:
        report = validate_runtime_overlay_assets(pack_root)
        print(json.dumps(report, indent=2))
        if report['decision'] == 'FAIL':
            raise SystemExit(1)
        return

    if not args.task or not args.file:
        parser.error('--task and --file are required unless using a validation-only flag')

    prompt = args.prompt
    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding='utf-8')
    output = Path(args.file).read_text(encoding='utf-8')
    report = validate_output(args.task, prompt, output, args.project_root)
    print(json.dumps(report, indent=2))
    if report['decision'] == 'FAIL':
        raise SystemExit(1)


if __name__ == '__main__':
    main()

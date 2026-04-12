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
PLACEHOLDER_PHRASES = ['placeholder', 'tbd', 'lorem ipsum', 'route is explicit', 'required sections are visible', 'evidence burden is named']
SUPERLATIVES = ['validated', 'proven', 'certified', 'best-in-class', 'compliant', 'externally validated', 'production-ready']
TRADEOFF_TOKENS = ['tradeoff', 'trade-off', 'instead of', 'rather than', 'preserve', 'sacrifice', 'compromise', 'flex first', 'tension', 'should win']
RATIONALE_TOKENS = ['because', 'so that', 'therefore', 'why', 'this matters']
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
    'measurable_threshold': [r'\bthreshold\b', r'\bscore\b', r'\bmetric\b', r'\bbenchmark\b', r'\bwcag\b', r'\bapca\b', r'\b\d+(?:\.\d+)?%\b', r'\b\d+(?:\.\d+)?:1\b'],
    'comparison_artifact': [r'\bbaseline\b', r'\bcomparison\b', r'\bcompare\b', r'\bversus\b', r'\bvs\b', r'\bbefore/after\b', r'\balternative\b', r'\bobvious alternative\b'],
    'state_or_behavior_rule': [r'\bstate\b', r'\bkeyboard\b', r'\bfocus\b', r'\bhierarchy\b', r'\bscan\b', r'\bflow\b', r'\border\b', r'\bbehavior\b', r'\bsequence\b', r'\bstate machine\b'],
    'implementation_constraint': [r'\bconstraint\b', r'\blimit\b', r'\bblocked\b', r'\bboundary\b', r'\brequires\b', r'\bdepends\b', r'\bonly if\b', r'\bpreserve\b', r'\bsafer path\b', r'\bintegration\b', r'\bdensity\b', r'\btoken\b', r'\balias\b', r'\bsemantic role\b', r'\bhex\b', r'\bgrid\b', r'\boverlay\b', r'\bhydration\b', r'\bbundle\b'],
    'file_backed_receipt': [r'\[file:', r'\bartifact\b', r'\blog\b', r'\bscorecard\b', r'\bfixture\b', r'\bvalidation result\b'],
    'benchmark_artifact': [r'\bbenchmark\b', r'\bscorecard\b', r'\beval\b', r'\bregression\b', r'\brun-\d+\b', r'\bbenchmark-run\b'],
    'reviewer_confidence_artifact': [r'\breviewer\b', r'\bconfidence\b', r'\bhuman review\b', r'\bexternal signal\b'],
    'standards_reference': [r'\bwcag\b', r'\bapca\b', r'\bpdf/ua\b', r'\baria\b', r'\bunicode\b', r'\breading order\b', r'\btag\b', r'\bartifact\b', r'\bcontrast\b', r'\brfc 9457\b', r'\bproblem details\b'],
    'permission_rule': [r'\bauth\b', r'\bpermission\b', r'\brole\b', r'\baccess\b', r'\binvite\b', r'\brevocation\b', r'\bapproval\b', r'\bbola\b', r'\bbfla\b', r'\btenant\b', r'\bobject-level\b'],
    'data_model_dependency': [r'\bdata model\b', r'\bschema\b', r'\bownership\b', r'\bfield\b', r'\brecord\b', r'\bobject\b', r'\btenant\b', r'\bmembership\b', r'\bretention\b', r'\bsource-of-truth\b', r'\bcanonical\b'],
    'verification_method': [r'\bverify\b', r'\bverification\b', r'\bcheck\b', r'\btest\b', r'\binspect\b', r'\bcopy-paste\b', r'\bextract\b', r'\bscreen reader\b', r'\boverlay\b', r'\bmeasurement\b', r'\bcompare\b', r'\bkeyboard only\b', r'\baxe\b'],
    'narrative_proof_boundary': [r'\bclaim\b', r'\bproof\b', r'\bproxy\b', r'\bmeasured\b', r'\bevidence\b', r'\bopen gap\b', r'\bexternal\b', r'\binternal\b'],
    'research_artifact': [r'\binterview\b', r'\bsurvey\b', r'\busability test\b', r'\bparticipant\b', r'\brespondent\b', r'\bsample\b', r'\btranscript\b', r'\bfield study\b', r'\bdiary\b', r'\bscreener\b'],
    'visual_structure_rule': [r'\bcomposition\b', r'\bfocal\b', r'\blegibility\b', r'\bdistance\b', r'\balignment\b', r'\brhythm\b', r'\bgrouping\b', r'\bscale\b', r'\bcontrast\b', r'\bproportion\b', r'\bthumbnail\b'],
    'rendering_boundary_rule': [r'\bserver component\b', r'\bclient component\b', r'\buse client\b', r'\bserver action\b', r'\bstatic\b', r'\bdynamic\b', r'\bppr\b', r'\bstreaming\b', r'\bsuspense\b', r'\bhydration\b'],
    'consistency_model': [r'\blinearizable\b', r'\bbounded staleness\b', r'\bread-your-writes\b', r'\brevision token\b', r'\bconsistency token\b', r'\bzedtoken\b', r'\bcursor\b', r'\bkeyset\b', r'\boutbox\b', r'\bmicro-batch\b'],
    'failure_semantics_rule': [r'\brfc 9457\b', r'\bproblem details\b', r'\bapplication/problem\+json\b', r'\btype\b', r'\btitle\b', r'\bstatus\b', r'\bdetail\b', r'\binstance\b'],
    'async_lifecycle_rule': [r'\bidempotency-key\b', r'\bfingerprint\b', r'\b409 conflict\b', r'\b422 unprocessable\b', r'\b400 bad request\b', r'\b202 accepted\b', r'\bstatus url\b', r'\bqueued\b', r'\brunning\b', r'\bterminal failure\b', r'\bterminal success\b'],
    'meaning_preservation_guard': [r'\bmeaning-preservation\b', r'\bmeaning guard\b', r'\bclaims preserved\b', r'\bargument preserved\b', r'\bdrift risk\b', r'\bmust stay unchanged\b'],
    'prose_quality_signal': [r'\bpattern\b', r'\brepeated\b', r'\bformulaic\b', r'\bnominalization\b', r'\btransition\b', r'\brhythm\b', r'\bverb logic\b', r'\bvoice\b', r'\bauthored texture\b'],
    'tier_behavior_rule': [r'\bfunctional\b', r'\bintegrative\b', r'\bstrategic\b', r'\bjargon\b', r'\bscaffolding\b', r'\bnext step\b'],
    'next_step_guidance': [r'\bnext step\b', r'\bstart with\b', r'\bfirst move\b', r'\bsafer next move\b', r'\bthen\b'],
    'resilience_rule': [r'\bcircuit breaker\b', r'\bbackoff\b', r'\bjitter\b', r'\bload shedding\b', r'\bgraceful degradation\b', r'\bcache-fallback\b', r'\bquota\b', r'\brate limit\b', r'\btrace_id\b', r'\bobservability\b']
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


def parse_sections(text: str) -> Dict[str, str]:
    sections: Dict[str, List[str]] = {'_root': []}
    current = '_root'
    for line in text.splitlines():
        m = re.match(r'^#{1,6}\s+(.+)$', line.strip())
        if m:
            current = m.group(1).strip().lower()
            sections.setdefault(current, [])
        else:
            sections.setdefault(current, []).append(line)
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


def detected_evidence_classes(text: str) -> Set[str]:
    low = text.lower()
    found = set()
    for class_id, patterns in EVIDENCE_CLASS_PATTERNS.items():
        if any(re.search(p, low, flags=re.IGNORECASE) for p in patterns):
            found.add(class_id)
    return found


def find_missing_decisions(task: Dict, low: str) -> List[Dict]:
    missing = []
    for dec in task.get('required_decisions', []):
        if isinstance(dec, dict) and not any(tok.lower() in low for tok in dec.get('any_of', [])):
            missing.append(dec)
    return missing


def find_missing_evidence_classes(task: Dict, classes_present: Set[str]) -> List[Dict]:
    missing = []
    for ev in task.get('required_evidence_classes', []):
        if ev['class_id'] not in classes_present:
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
    if route_id and not (pack_root / 'src' / 'runtime' / 'cards' / 'routes' / f'{route_id}.json').exists():
        statuses.append({'class': 'missing_runtime_card_with_canonical_fallback', 'action': 'continue_with_canonical', 'detail': f'missing runtime route card {route_id}'})
    if task_id and not (pack_root / 'src' / 'runtime' / 'cards' / 'contracts' / f'{task_id}.json').exists():
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
        if not (pack_root / 'src' / 'runtime' / 'cards' / 'routes' / f'{route}.json').exists():
            errors.append(f'missing runtime route card: {route}')
    for task in task_ids:
        if not (pack_root / 'src' / 'runtime' / 'cards' / 'contracts' / f'{task}.json').exists():
            errors.append(f'missing runtime contract card: {task}')

    for rel in ['src/operator/protocols/DEGRADED_MODE_PROTOCOL.md', 'src/operator/protocols/VISUAL_INPUT_PROTOCOL.md', 'src/operator/protocols/LIGHTWEIGHT_RESPONSE_PROTOCOL.md', 'QUICKSTART.md']:
        if not (pack_root / rel).exists():
            errors.append(f'{rel} missing')

    control_map = (pack_root / 'src' / 'operator' / 'governance' / 'CONTROL_AUTHORITY_MAP.md').read_text(encoding='utf-8').lower()
    if 'human-readable mirrors — maintenance/debug only' not in control_map:
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
    low = prompt.lower()
    return any(tok in low for tok in ['screenshot', 'mockup', 'image', 'page image', 'from a screenshot'])

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
    findings = ''
    recs = ''
    for name, content in sections.items():
        lname = name.lower()
        if any(x in lname for x in ['finding', 'key failures', 'problem framing', 'dashboard role', 'source constraints']):
            findings += ' ' + content
        if any(x in lname for x in ['recommend', 'rebuild path', 'rebuild sequence', 'recommendations']):
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


def validate_output(task_id: str, prompt: str, output: str, project_root: str = '') -> Dict:
    task = get_task(task_id)
    issues = []
    warnings = []
    sections = parse_sections(output)
    density = information_density(output)
    overlap = prompt_overlap(prompt, output)
    evidence = evidence_count(output)
    total_content_words = section_word_count(output)
    weight = lightweight_class(task, prompt)
    min_total_words = sum(sec['min_words'] for sec in task['required_sections'])
    if weight == 'lightweight':
        min_total_words = int(min_total_words * 0.7)
    score = 100
    low = output.lower()
    classes_present = detected_evidence_classes(output)

    for phrase in PLACEHOLDER_PHRASES:
        if phrase in low:
            issues.append({'id': 'placeholder_text', 'severity': 'hard', 'detail': f'placeholder phrase present: {phrase}'})
            score -= 20

    for req in task['required_sections']:
        heading = req['name'].lower()
        match = None
        for sec_name, content in sections.items():
            if heading in sec_name:
                match = content
                break
        if match is None:
            issues.append({'id': 'missing_section', 'severity': 'hard', 'detail': f'missing section: {req["name"]}'})
            score -= 12
        else:
            count = section_word_count(match)
            required_words = int(req['min_words'] * (0.75 if weight == 'lightweight' else 1.0))
            if count < required_words:
                issues.append({'id': 'thin_section', 'severity': 'hard', 'detail': f'section {req["name"]} too thin: {count} < {required_words}'})
                score -= 10

    if density < task['min_density'] or total_content_words < int(min_total_words * 0.7):
        issues.append({'id': 'low_information_density', 'severity': 'hard', 'detail': f'density {density} / content words {total_content_words} below expected depth {int(min_total_words * 0.7)}'})
        score -= 12
    if (overlap > 0.55 and len(tokenize(output)) < 220) or (overlap > 0.25 and total_content_words < int(min_total_words * 0.9)):
        issues.append({'id': 'prompt_restatement', 'severity': 'hard', 'detail': f'prompt overlap too high for the amount of transformation: {overlap:.2f}'})
        score -= 12

    required_evidence = max(1, task['required_evidence_count'] - (1 if weight == 'lightweight' else 0))
    if evidence < required_evidence:
        issues.append({'id': 'insufficient_evidence', 'severity': 'hard', 'detail': f'evidence count {evidence} below required {required_evidence}'})
        score -= 12
    if task.get('require_tradeoff') and not any(tok in low for tok in TRADEOFF_TOKENS):
        issues.append({'id': 'missing_tradeoff', 'severity': 'hard', 'detail': 'no explicit tradeoff language found'})
        score -= 10
    if fake_tradeoff(low):
        issues.append({'id': 'fake_tradeoff', 'severity': 'hard', 'detail': 'tradeoff language is present without both gain and sacrifice'})
        score -= 10
    if task.get('require_rationale') and not any(tok in low for tok in RATIONALE_TOKENS):
        issues.append({'id': 'missing_rationale', 'severity': 'hard', 'detail': 'no explicit rationale language found'})
        score -= 10
    if task.get('require_alternatives') and not any(tok in low for tok in ALTERNATIVE_TOKENS):
        warnings.append({'id': 'missing_alternative', 'severity': 'soft', 'detail': 'no alternative path was named'})
        score -= 4

    if ('functional' in low or 'integrative' in low) and not any(tok in low for tok in ['next step', 'start with', 'first move', 'safer next move', 'then']):
        warnings.append({'id': 'missing_next_step_guidance', 'severity': 'soft', 'detail': 'designer-readable guidance is missing a visible next move'})
        score -= 4

    if task_id == 'text_humanization_revision' and not any(tok in low for tok in ['meaning-preservation', 'meaning guard', 'claims preserved', 'argument preserved', 'drift risk']):
        issues.append({'id': 'missing_meaning_guard', 'severity': 'hard', 'detail': 'text humanization requires a visible meaning-preservation guard'})
        score -= 10

    visual_prompt = prompt_has_visual(prompt)
    raw_missing_decisions = find_missing_decisions(task, low)
    missing_decisions = []
    for dec in raw_missing_decisions:
        if dec.get('id') == 'visual_confidence_boundary' and not visual_prompt:
            continue
        missing_decisions.append(dec)
    for dec in missing_decisions:
        issues.append({'id': 'missing_required_decision', 'severity': 'hard', 'detail': f"missing required decision `{dec['id']}`: {dec['description']}"})
        score -= 8

    raw_missing_classes = find_missing_evidence_classes(task, classes_present)
    missing_classes = []
    for ev in raw_missing_classes:
        if ev.get('class_id') == 'visual_structure_rule' and not visual_prompt:
            continue
        missing_classes.append(ev)
    for ev in missing_classes:
        issues.append({'id': 'missing_evidence_class', 'severity': 'hard', 'detail': f"missing evidence class `{ev['class_id']}`: {ev['description']}"})
        score -= 8

    for item in task.get('forbidden_shortcuts', []):
        if any(p.lower() in low for p in item.get('patterns', [])):
            issues.append({'id': 'forbidden_shortcut', 'severity': 'hard', 'detail': f"forbidden shortcut `{item['id']}` triggered"})
            score -= 10

    for item in task.get('overclaim_rules', []):
        forbidden_hit = [term for term in item.get('forbidden_terms', []) if term.lower() in low]
        if forbidden_hit and not any(term.lower() in low for term in item.get('allowed_if_any', [])):
            issues.append({'id': 'overclaim_without_evidence', 'severity': 'hard', 'detail': f"overclaim rule `{item['id']}` triggered by: {', '.join(forbidden_hit)}"})
            score -= 10

    for word in SUPERLATIVES:
        if word in low and not ({'measurable_threshold', 'benchmark_artifact', 'file_backed_receipt', 'reviewer_confidence_artifact'} & classes_present):
            issues.append({'id': 'unsupported_superlative', 'severity': 'hard', 'detail': f'{word} used without the required proof class'})
            score -= 10

    if unsupported_specificity(low, classes_present):
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
        if pat.lower() in low:
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
    return {
        'task_id': task_id,
        'task_weight': weight,
        'density': density,
        'prompt_overlap': round(overlap, 3),
        'evidence_count': evidence,
        'evidence_classes_present': sorted(classes_present),
        'issues': issues,
        'warnings': warnings,
        'score': max(0, score),
        'decision': decision,
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

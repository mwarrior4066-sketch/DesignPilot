#!/usr/bin/env python3
"""Shared authority helpers for DesignPilot maintainer scripts.

This module intentionally stays small in Part 1.
It centralizes canonical surface pointers so later script changes can import
one place instead of hard-coding authority paths repeatedly.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
PACK_MANIFEST_PATH = ROOT / 'PACK_MANIFEST.json'
AUTHORITY_MANIFEST_PATH = ROOT / 'config' / 'authority_manifest.yaml'


def load_pack_manifest() -> Dict[str, Any]:
    return json.loads(PACK_MANIFEST_PATH.read_text(encoding='utf-8'))


def load_authority_manifest() -> Dict[str, Any]:
    return yaml.safe_load(AUTHORITY_MANIFEST_PATH.read_text(encoding='utf-8')) or {}


def authority_section(name: str) -> Dict[str, Any]:
    return dict(load_authority_manifest().get('authorities', {}).get(name, {}))


def generated_outputs() -> list[str]:
    return list(load_authority_manifest().get('ownership', {}).get('generated_outputs', []))


def authoritative_inputs() -> list[str]:
    return list(load_authority_manifest().get('ownership', {}).get('authoritative_inputs', []))

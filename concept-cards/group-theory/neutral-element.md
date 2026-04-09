---
# === CORE IDENTIFICATION ===
concept: Neutral Element
slug: neutral-element

# === CLASSIFICATION ===
category: group-fundamentals
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 6
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - identity element
  - unit element

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - inverse-element
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the identity element of a group?"
  - "Is the neutral element of a group unique?"
---

# Quick Definition

The neutral element (or identity element) of a group G is the unique element e such that a * e = a = e * a for all a in G. It is denoted 1 in multiplicative notation or 0 in additive notation.

# Core Definition

An element e satisfying a * e = a = e * a for all a in G is called a **neutral element** (Definition 1.1, axiom G2, p. 6). The neutral element is unique: if e' is a second such element, then e' = e * e' = e (1.2a, p. 7). Moreover, e is the unique element of G satisfying x * x = x (1.2a, p. 7).

# Prerequisites

- **Group** — the neutral element is one of the three axioms defining a group

# Key Properties

1. The neutral element is unique in any group (1.2a)
2. It is the unique idempotent element: the only element satisfying x * x = x (1.2a)
3. e * a = a = a * e for all a in G (two-sided identity)
4. In multiplicative notation it is written 1; in additive notation it is written 0

# Construction / Recognition

## To Recognize:
1. Find an element e such that e * a = a for all a in G (left identity)
2. Verify that a * e = a for all a in G (right identity)
3. Alternatively, find the unique element satisfying e * e = e

# Context & Application

The neutral element is a required component of the group axioms (G2). Its existence and uniqueness are among the first results proved about groups. The empty product of elements in a group equals the neutral element (Remark 1.9, p. 10).

# Examples

**Example 1** (p. 8, 1.3): In (Z, +), the neutral element is 0.

**Example 2** (p. 8, 1.4): In Sym(S), the neutral element is the identity map s -> s.

**Example 3** (p. 9, 1.7): In GL_n(F), the neutral element is the n x n identity matrix.

# Relationships

## Builds Upon
- **group** — neutral element is axiom G2

## Enables
- **inverse-element** — inverses are defined relative to the neutral element
- **subgroup** — every subgroup must contain the neutral element

## Related
- **monoid** — a semigroup with a neutral element (but not necessarily inverses)

# Common Errors

- **Error**: Assuming any left identity is the neutral element without verifying the right identity property
  **Correction**: In a group, left identity implies right identity (Aside 1.10a), but this requires proof

# Common Confusions

- **Confusion**: Thinking a group can have multiple identity elements
  **Clarification**: The neutral element is always unique; the proof is immediate (e' = e * e' = e)

# Source Reference

Chapter 1: Basic Definitions and Results, Definition 1.1 axiom G2 (p. 6) and Remark 1.2a (p. 7).

# Verification Notes

- Definition source: Direct from Definition 1.1 (G2) and 1.2a
- Confidence rationale: HIGH — explicitly defined and uniqueness proved
- Uncertainties: None
- Cross-reference status: Verified against planned cards

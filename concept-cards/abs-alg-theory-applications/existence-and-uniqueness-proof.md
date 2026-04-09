---
# === CORE IDENTIFICATION ===
concept: Existence and Uniqueness Proof
slug: existence-and-uniqueness-proof

# === CLASSIFICATION ===
category: foundations
subcategory: logic-and-proofs
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 15
section: "A Short Note on Proofs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mathematical-proof
extends: []
related:
  - identity-element-uniqueness
  - inverse-uniqueness
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

An existence and uniqueness proof has two parts: first show that an object with the desired properties exists, then show it is the only such object.

# Core Definition

"Suppose you wish to show that an object exists and is unique. First show that there actually is such an object. To show that it is unique, assume that there are two such objects, say $r$ and $s$, and then show that $r = s$" (Judson, p. 15).

# Prerequisites

- **Mathematical proof** — This is a proof technique

# Key Properties

1. Two-part structure: existence + uniqueness
2. Existence: construct or demonstrate the object
3. Uniqueness: assume two objects and show they are equal
4. Used extensively in group theory (identity, inverses, GCD)

# Context & Application

This proof technique appears throughout abstract algebra: uniqueness of the identity element (Proposition 3.17), uniqueness of inverses (Proposition 3.18), uniqueness of the GCD, and the Division Algorithm (existence and uniqueness of quotient and remainder).

# Examples

**Example 1** (p. 33): The Division Algorithm proof has this structure: first prove existence of $q$ and $r$ using the Well-Ordering Principle, then prove uniqueness by assuming two such pairs and showing they are equal.

**Example 2** (p. 49): Identity uniqueness: if $e$ and $e'$ are both identities, then $e = ee' = e'$.

# Relationships

## Builds Upon
- **mathematical-proof** — A proof technique

## Related
- **identity-element-uniqueness** — Uses this technique
- **inverse-uniqueness** — Uses this technique

# Source Reference

Chapter 1: Preliminaries, Section 1.1, page 15.

# Verification Notes

- Definition source: Direct quote from p. 15
- Confidence: HIGH — explicit description
- Cross-reference status: Verified
- Uncertainties: None

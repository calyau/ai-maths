---
# === CORE IDENTIFICATION ===
concept: Base Field
slug: base-field

# === CLASSIFICATION ===
category: field-theory
subcategory: field-extensions
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.1 Extension Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ground field"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - field
extends: []
related:
  - extension-field
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the base field of a field extension?"
---

# Quick Definition

In a field extension $E/F$, the smaller field $F$ is called the base field (or ground field). It is the field being extended.

# Core Definition

When $E$ is an extension field of $F$, the field $F$ is called the **base field** (Judson, p. 274).

# Prerequisites

- **Field** — The base field is a field

# Key Properties

1. The base field $F$ is a subfield of the extension $E$
2. Elements of the base field are fixed by all Galois group automorphisms: $E_{G(E/F)} = F$ for Galois extensions
3. The degree $[E:F]$ measures the "size" of the extension relative to the base field
4. Algebraicity and transcendence of elements are defined relative to the base field

# Context & Application

The base field is the starting point from which extensions are built. The same field can be a base field in one context and an extension in another (e.g., $\mathbb{Q}$ is the base field for $\mathbb{Q}(\sqrt{2})$, and $\mathbb{Q}(\sqrt{2})$ is the base field for $\mathbb{Q}(\sqrt{2}, i)$).

# Examples

**Example 1** (p. 274): $\mathbb{Q}$ is the base field in the extension $\mathbb{Q}(\sqrt{2})/\mathbb{Q}$.

**Example 2** (p. 278): $\mathbb{R}$ is the base field in $\mathbb{C}/\mathbb{R}$.

# Relationships

## Related
- **Extension field** — The extension is built over the base field

# Source Reference

Chapter 21: Fields, Section 21.1, page 274.

# Verification Notes

- Definition source: Direct from p. 274
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None

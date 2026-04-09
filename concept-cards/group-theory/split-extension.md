---
# === CORE IDENTIFICATION ===
concept: Split Extension
slug: split-extension

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: extensions
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 50
section: "Extensions of groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-of-groups
  - semidirect-product
extends:
  - extension-of-groups
related:
  - schur-zassenhaus-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a split extension?"
  - "When does a group extension split?"
---

# Quick Definition

A split extension is an extension $1 \to N \to G \to Q \to 1$ that is isomorphic to one defined by a semidirect product $N \rtimes_\theta Q$.

# Core Definition

An extension $1 \to N \xrightarrow{\iota} G \xrightarrow{\pi} Q \to 1$ is split if there exists a homomorphism $s: Q \to G$ with $\pi \circ s = \operatorname{id}_Q$ (Milne, p. 50). Equivalently, there exists a subgroup $Q' \subset G$ such that $\pi$ restricts to an isomorphism $Q' \to Q$.

# Prerequisites

- **Extension of groups** — A split extension is a special extension
- **Semidirect product** — Split extensions are exactly semidirect products

# Key Properties

1. Equivalent conditions for splitting: (a) section $s: Q \to G$ exists, (b) complement $Q' \leq G$ with $\pi|_{Q'}: Q' \xrightarrow{\sim} Q$
2. Every semidirect product defines a split extension, and conversely
3. Extensions by complete normal subgroups always split as direct products (Proposition 3.22)

# Examples

**Example 1** (p. 46): $1 \to A_n \to S_n \to C_2 \to 1$ splits via $s: C_2 \hookrightarrow S_n$, $s(1) = (12)$.

**Non-Example** (p. 50): $1 \to C_p \to C_{p^2} \to C_p \to 1$ does not split.

# Relationships

## Builds Upon
- **extension-of-groups**, **semidirect-product**

## Related
- **schur-zassenhaus-theorem** — Guarantees splitting for coprime orders

# Source Reference

Chapter 3: Automorphisms and Extensions, "Extensions of groups", page 50.

# Verification Notes

- Definition source: Direct from p. 50
- Confidence: HIGH — explicit definition
- Uncertainties: None

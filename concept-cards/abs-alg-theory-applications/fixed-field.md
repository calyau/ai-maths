---
# === CORE IDENTIFICATION ===
concept: Fixed Field
slug: fixed-field

# === CLASSIFICATION ===
category: galois-theory
subcategory: field-automorphisms
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.2 The Fundamental Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "invariant field"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - field-automorphism
  - galois-group
extends: []
related:
  - fundamental-theorem-of-galois-theory
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the fixed field of a group of automorphisms?"
---

# Quick Definition

The fixed field of a collection of automorphisms $\{\sigma_i\}$ of a field $F$ is the subfield of all elements left unchanged by every $\sigma_i$: $F_{\{\sigma_i\}} = \{a \in F : \sigma_i(a) = a \text{ for all } \sigma_i\}$.

# Core Definition

Let $\{\sigma_i : i \in I\}$ be a collection of automorphisms of a field $F$. Then

$$F_{\{\sigma_i\}} = \{a \in F : \sigma_i(a) = a \text{ for all } \sigma_i\}$$

is a subfield of $F$ (Proposition 23.14, Judson, p. 311). The field fixed by a subgroup $G$ of $\operatorname{Aut}(F)$ is denoted $F_G$ (Corollary 23.15, p. 312).

# Prerequisites

- **Field automorphism** — Fixed fields are defined relative to automorphisms
- **Galois group** — The fixed field of the Galois group gives back the base field

# Key Properties

1. $F_{\{\sigma_i\}}$ is always a subfield (Proposition 23.14)
2. If $E$ is the splitting field of a separable polynomial over $F$, then $E_{G(E/F)} = F$ (Proposition 23.17)
3. $[E:F] \leq |G|$ when $F = E_G$ (Lemma 23.18, Artin's Lemma)
4. The correspondence $G \mapsto E_G$ is one half of the Galois correspondence

# Context & Application

Fixed fields provide the connection between subgroups of the Galois group and intermediate fields. The map $G \mapsto E_G$ (from subgroups to fixed fields) is one direction of the Galois correspondence. The other direction sends an intermediate field $K$ to the subgroup $G(E/K)$.

# Examples

**Example 1** (p. 312): In $\mathbb{Q}(\sqrt{3}, \sqrt{5})$, the automorphism $\sigma$ mapping $\sqrt{3} \mapsto -\sqrt{3}$ has fixed field $\mathbb{Q}(\sqrt{5})$.

**Example 2** (p. 314): The full Galois group $G(\mathbb{Q}(\sqrt{3}, \sqrt{5})/\mathbb{Q})$ has fixed field $\mathbb{Q}$.

# Relationships

## Builds Upon
- **Field automorphism** — Fixed fields are defined relative to automorphisms
- **Galois group** — $E_{G(E/F)} = F$ for Galois extensions

## Enables
- **Fundamental Theorem of Galois Theory** — Uses the fixed field correspondence

# Source Reference

Chapter 23: Galois Theory, Section 23.2, pages 311–313. See Propositions 23.14, 23.17, Lemma 23.18.

# Verification Notes

- Definition source: Direct from Proposition 23.14, p. 311
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None

---
# === CORE IDENTIFICATION ===
concept: Semidirect Product Isomorphism Criteria
slug: semidirect-product-isomorphism-criteria

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: products
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 48
section: "Criteria for semidirect products to be isomorphic"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semidirect-product
  - automorphism-group
extends:
  - semidirect-product
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When do two semidirect products give isomorphic groups?"
---

# Quick Definition

Two semidirect products $N \rtimes_\theta Q$ and $N \rtimes_{\theta'} Q$ are isomorphic under specific conditions involving automorphisms of $N$ or $Q$.

# Core Definition

Three criteria (Milne, Lemmas 3.17-3.19, pp. 48-49):

- **Lemma 3.17**: If there exists $\alpha \in \operatorname{Aut}(N)$ with $\theta'(q) = \alpha \circ \theta(q) \circ \alpha^{-1}$ for all $q$, then $(n,q) \mapsto (\alpha(n), q)$ is an isomorphism.
- **Lemma 3.18**: If $\theta = \theta' \circ \alpha$ with $\alpha \in \operatorname{Aut}(Q)$, then $(n,q) \mapsto (n, \alpha(q))$ is an isomorphism.
- **Lemma 3.19**: If $Q$ is finite cyclic and $\theta(Q)$ is conjugate to $\theta'(Q)$ in $\operatorname{Aut}(N)$, then $N \rtimes_\theta Q \approx N \rtimes_{\theta'} Q$.

# Prerequisites

- **Semidirect product** — The objects being compared
- **Automorphism group** — Criteria involve $\operatorname{Aut}(N)$ and $\operatorname{Aut}(Q)$

# Key Properties

1. Lemma 3.19 requires $Q$ to be finite; it fails for $Q$ infinite (counterexample with $C_{25} \rtimes C_\infty$, p. 49)
2. Summary 3.20 distinguishes: both normal $\Rightarrow$ direct product; one normal $\Rightarrow$ semidirect; neither normal $\Rightarrow$ Zappa-Szep product

# Context & Application

These criteria are essential for classifying groups of small order, where multiple homomorphisms $\theta$ may yield isomorphic groups.

# Examples

**Example 1** (p. 47): $D_4 \approx C_4 \rtimes C_2 \approx (C_2 \times C_2) \rtimes C_2$ — the same group has different semidirect product decompositions.

# Source Reference

Chapter 3: Automorphisms and Extensions, "Criteria for semidirect products to be isomorphic", Lemmas 3.17-3.19, pages 48-49.

# Verification Notes

- Definition source: Lemmas 3.17-3.19
- Confidence: HIGH — explicit statements with proofs
- Uncertainties: None

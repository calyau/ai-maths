---
concept: Conjugation Action on Subgroups
slug: conjugate-subgroups-action
category: group-structure
subcategory: sylow-theory
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Sylow Theorems"
chapter_number: 15
pdf_page: 196
section: "The Sylow Theorems"
extraction_confidence: high
aliases: []
prerequisites:
  - group-action
  - conjugation-of-subgroups
extends:
  - group-action
related:
  - normalizer
  - second-sylow-theorem
contrasts_with: []
answers_questions:
  - "How does a group act on the collection of its subgroups by conjugation?"
---

# Quick Definition

For a group $G$, let $\mathcal{S}$ be the collection of all subgroups. A subgroup $H$ acts on $\mathcal{S}$ by conjugation: $h \cdot K = hKh^{-1}$. The stabilizer of $K$ is $N(K) \cap H$, and the number of $H$-conjugates of $K$ is $[H : N(K) \cap H]$.

# Core Definition

"For a group $G$, let $\mathcal{S}$ be the collection of all subgroups of $G$. For any subgroup $H$, $\mathcal{S}$ is a $H$-set, where $H$ acts on $\mathcal{S}$ by conjugation" via $h \cdot K \mapsto hKh^{-1}$ (Judson, p. 196).

**Lemma 15.6**: "Let $H$ and $K$ be subgroups of $G$. The number of distinct $H$-conjugates of $K$ is $[H : N(K) \cap H]$" (p. 197).

# Prerequisites

- **Group action** — This is a specific action
- **Conjugation of subgroups** — The action mechanism

# Key Properties

1. The stabilizer of $K$ under $H$-conjugation is $N(K) \cap H$
2. Number of $H$-conjugates of $K$ = $[H : N(K) \cap H]$ (Lemma 15.6)
3. Under $G$-conjugation: number of conjugates of $K$ = $[G : N(K)]$
4. Central to the proof of the Second Sylow Theorem

# Relationships

## Builds Upon
- **Group action** — Action of $H$ on subgroups

## Enables
- **Second Sylow theorem** — Uses this action to prove conjugacy

## Related
- **Normalizer** — Stabilizer of $K$ under conjugation is $N(K)$

# Source Reference

Chapter 15: The Sylow Theorems, Section 15.1, p. 196-197. Lemma 15.6.

# Verification Notes

- Definition source: p. 196 and Lemma 15.6
- Confidence: HIGH

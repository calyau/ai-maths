---
# === CORE IDENTIFICATION ===
concept: Divisibility Chain
slug: divisibility-chain

# === CLASSIFICATION ===
category: abelian-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Finitely Generated Abelian Groups"
chapter_number: 21
pdf_page: 126
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "divisibility condition"
  - "m_1 | m_2 | ... | m_k"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-fg-abelian-groups
extends: []
related:
  - torsion-coefficients
  - smith-normal-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the divisibility chain condition in the classification of f.g. abelian groups?"
  - "Why must the torsion coefficients satisfy m_1 | m_2 | ... | m_k?"
---

# Quick Definition

The divisibility chain $m_1 \mid m_2 \mid \cdots \mid m_k$ is the condition on torsion coefficients in the canonical decomposition of a finitely generated abelian group. It ensures uniqueness of the decomposition and arises naturally from the proof of Theorem 21.1.

# Core Definition

In the classification theorem (21.1), the torsion coefficients satisfy $m_i \mid m_{i+1}$ for $1 \le i \le k - 1$. This divisibility chain is essential: without it, different decompositions could represent the same group. For example, $\mathbb{Z}_2 \times \mathbb{Z}_3 \cong \mathbb{Z}_6$ but only the latter is in canonical form since $2 \mid 3$ fails (Armstrong, pp. 126--127).

# Prerequisites

- **Classification of f.g. abelian groups** -- the divisibility chain is part of the canonical form

# Key Properties

1. The divisibility chain ensures uniqueness of the torsion coefficients
2. In the proof, $m_1$ is the smallest positive exponent in any relation for any minimal generating set; $m_1 \mid m_2$ because of a division-algorithm argument
3. The Smith normal form diagonal entries automatically satisfy the chain
4. If a decomposition does not satisfy the chain (e.g., $\mathbb{Z}_6 \times \mathbb{Z}_{10}$), it can be converted: $\mathbb{Z}_6 \times \mathbb{Z}_{10} \cong \mathbb{Z}_2 \times \mathbb{Z}_{30}$

# Context & Application

The divisibility chain distinguishes Armstrong's (and the classical) approach from the prime-power decomposition. Both are valid canonical forms, but the divisibility chain form is the one produced by Smith normal form.

# Relationships

## Builds Upon
- **Classification of f.g. abelian groups** -- the divisibility chain is part of the theorem

## Related
- **Torsion coefficients** -- must satisfy the chain
- **Smith normal form** -- produces diagonal entries satisfying the chain

# Common Errors

- **Error**: Accepting $\mathbb{Z}_4 \times \mathbb{Z}_6$ as canonical because $4 \mid 6$ is false -- wait, actually $4 \nmid 6$.
  **Correction**: $\mathbb{Z}_4 \times \mathbb{Z}_6$ is not in canonical form since $4 \nmid 6$. Rewrite as $\mathbb{Z}_2 \times \mathbb{Z}_{12}$ (where $2 \mid 12$).

# Source Reference

Chapter 21: Finitely Generated Abelian Groups, Theorem 21.1, pages 126--129.

# Verification Notes

- Definition: From Theorem 21.1, p. 126
- Confidence: HIGH -- central condition in the theorem

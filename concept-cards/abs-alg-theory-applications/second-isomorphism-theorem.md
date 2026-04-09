---
# === CORE IDENTIFICATION ===
concept: Second Isomorphism Theorem
slug: second-isomorphism-theorem

# === CLASSIFICATION ===
category: morphisms
subcategory: isomorphism-theorems
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Homomorphisms"
chapter_number: 11
pdf_page: 149
section: "The Isomorphism Theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "diamond isomorphism theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - factor-group
  - first-isomorphism-theorem
extends:
  - first-isomorphism-theorem
related:
  - third-isomorphism-theorem
  - correspondence-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Second Isomorphism Theorem?"
  - "How do subgroups and normal subgroups interact to produce isomorphisms?"
---

# Quick Definition

The Second Isomorphism Theorem states that if $H$ is a subgroup and $N$ is a normal subgroup of $G$, then $HN$ is a subgroup, $H \cap N$ is normal in $H$, and $H/(H \cap N) \cong HN/N$.

# Core Definition

**Theorem 11.12 (Second Isomorphism Theorem)**: "Let $H$ be a subgroup of a group $G$ (not necessarily normal in $G$) and $N$ a normal subgroup of $G$. Then $HN$ is a subgroup of $G$, $H \cap N$ is a normal subgroup of $H$, and $H/H \cap N \cong HN/N$" (Judson, p. 149).

# Prerequisites

- **Normal subgroup** — $N$ must be normal in $G$
- **Factor group** — Both $H/(H \cap N)$ and $HN/N$ are factor groups
- **First isomorphism theorem** — Used in the proof

# Key Properties

1. $HN = \{hn : h \in H, n \in N\}$ is a subgroup of $G$
2. $H \cap N$ is a normal subgroup of $H$
3. $H/(H \cap N) \cong HN/N$
4. The isomorphism is induced by the map $h \mapsto hN$
5. $N$ need not be normal in $HN$ for the theorem to work — it is because $N$ is normal in $G$

# Construction / Recognition

## To Apply the Second Isomorphism Theorem:
1. Identify a subgroup $H$ and a normal subgroup $N$ of $G$
2. Form $HN$ (verify it is a subgroup — guaranteed by the theorem)
3. Compute $H \cap N$
4. Conclude $H/(H \cap N) \cong HN/N$

# Context & Application

The Second Isomorphism Theorem is used in the proof of the Jordan-Holder theorem and in analyzing how subgroups interact with normal subgroups. It provides a way to relate quotients of different subgroups.

# Examples

**Example 1** (Exercise 11.4.7, p. 152): In $\mathbb{Z}_{24}$, let $H = \langle 4 \rangle = \{0, 4, 8, 12, 16, 20\}$ and $N = \langle 6 \rangle = \{0, 6, 12, 18\}$. Then $H + N$, $H \cap N$, $HN/N$, and $H/(H \cap N)$ can be computed explicitly to verify the isomorphism.

# Relationships

## Builds Upon
- **First isomorphism theorem** — The proof uses the First Isomorphism Theorem with the map $h \mapsto hN$

## Enables
- **Jordan-Holder theorem** — Uses the Second Isomorphism Theorem in its proof

## Related
- **Third isomorphism theorem** — Another structural theorem about quotients

# Common Errors

- **Error**: Assuming $H$ must be normal in $G$
  **Correction**: Only $N$ needs to be normal in $G$; $H$ is an arbitrary subgroup

# Common Confusions

- **Confusion**: Confusing which group $H \cap N$ is normal in
  **Clarification**: $H \cap N$ is normal in $H$, not necessarily in $G$

# Source Reference

Chapter 11: Homomorphisms, Section 11.2, pages 149-150. Theorem 11.12.

# Verification Notes

- Definition source: Direct quote of Theorem 11.12
- Proof: Complete proof in source
- Confidence: HIGH — major theorem with full proof
- Cross-reference status: Verified

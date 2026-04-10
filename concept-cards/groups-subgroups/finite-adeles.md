---
# === CORE IDENTIFICATION ===
concept: Finite Adèles
slug: finite-adeles

# === CLASSIFICATION ===
category: arithmetic-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Arithmetic Subgroups"
chapter_number: 7
pdf_page: 401
section: "Adèlic description of congruence subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - ring of finite adèles
  - "A_f"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - p-adic-numbers
extends: []
related:
  - adelic-description-of-congruence-subgroups
  - congruence-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding arithmetic subgroups?"
---

# Quick Definition

The ring of finite adèles $\mathbb{A}_f$ is the restricted product $\prod(\mathbb{Q}_\ell : \mathbb{Z}_\ell)$ over all finite primes $\ell$, consisting of sequences $(a_\ell)$ with $a_\ell \in \mathbb{Z}_\ell$ for almost all $\ell$.

# Core Definition

"The *ring of finite adèles* is the restricted topological product $\mathbb{A}_f = \prod(\mathbb{Q}_\ell : \mathbb{Z}_\ell)$ where $\ell$ runs over the finite primes of $\mathbb{Q}$. Thus, $\mathbb{A}_f$ is the subring of $\prod \mathbb{Q}_\ell$ consisting of the $(a_\ell)$ such that $a_\ell \in \mathbb{Z}_\ell$ for almost all $\ell$, and it is endowed with the topology for which $\prod \mathbb{Z}_\ell$ is open and has the product topology." (Milne, p. 401)

For an algebraic group $G$ over $\mathbb{Q}$, one defines $G(\mathbb{A}_f) = \prod(G(\mathbb{Q}_\ell) : G(\mathbb{Z}_\ell))$, which is a topological group.

# Prerequisites

- **$p$-adic numbers** — the finite adèles are built from $\mathbb{Q}_\ell$ and $\mathbb{Z}_\ell$

# Key Properties

1. $\mathbb{A}_f$ is a topological ring with $\prod \mathbb{Z}_\ell$ as a compact open subring
2. $\mathbb{G}_m(\mathbb{A}_f) = \prod(\mathbb{Q}_\ell^\times : \mathbb{Z}_\ell^\times) = \mathbb{A}_f^\times$
3. $G(\mathbb{A}_f)$ is a locally compact topological group for any algebraic group $G$
4. The definition of $G(\mathbb{Z}_\ell)$ depends on a choice of presentation, but $G(\mathbb{A}_f)$ does not
5. Compact open subgroups of $G(\mathbb{A}_f)$ correspond to congruence subgroups of $G(\mathbb{Q})$

# Construction / Recognition

## To Construct $G(\mathbb{A}_f)$:
1. Choose an embedding $G \hookrightarrow \mathrm{GL}_n$
2. For each prime $\ell$, this determines $G(\mathbb{Z}_\ell) = G(\mathbb{Q}_\ell) \cap \mathrm{GL}_n(\mathbb{Z}_\ell)$
3. Form the restricted product $G(\mathbb{A}_f) = \prod(G(\mathbb{Q}_\ell) : G(\mathbb{Z}_\ell))$

# Context & Application

The adèlic viewpoint provides a uniform framework for studying congruence subgroups at all primes simultaneously. A congruence condition at a prime $\ell$ corresponds to shrinking the local component from $G(\mathbb{Z}_\ell)$ to a smaller open subgroup. The adèlic language is essential for the modern theory of automorphic forms and Shimura varieties.

# Examples

**Example 1** (p. 401): $\mathbb{G}_m(\mathbb{A}_f) = \mathbb{A}_f^\times = \prod(\mathbb{Q}_\ell^\times : \mathbb{Z}_\ell^\times)$.

**Example 2** (p. 401): For $G \hookrightarrow \mathrm{GL}_n$, the compact open subgroup $K(N) = \prod K_\ell$ where $K_\ell = G(\mathbb{Z}_\ell)$ for $\ell \nmid N$ and $K_\ell = \{g \in G(\mathbb{Z}_\ell) \mid g \equiv I \bmod \ell^{r_\ell}\}$ for $r_\ell = \mathrm{ord}_\ell(N)$, satisfies $K(N) \cap G(\mathbb{Q}) = \Gamma(N)$.

# Relationships

## Enables
- **Adelic description of congruence subgroups** — congruence subgroups correspond to compact open subgroups of $G(\mathbb{A}_f)$
- **Connected Shimura variety** — the adèlic viewpoint is essential for canonical models

## Related
- **Congruence subgroup** — the adèlic description characterizes congruence subgroups

# Common Errors

- **Error**: Confusing the restricted product with the full product
  **Correction**: The restricted product requires $a_\ell \in \mathbb{Z}_\ell$ for *almost all* $\ell$, not just some

# Common Confusions

- **Confusion**: Thinking $G(\mathbb{A}_f)$ depends on the choice of embedding
  **Clarification**: Different embeddings give the same $G(\mathbb{Z}_\ell)$ for almost all $\ell$, so the restricted product is independent of choices

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 6, pages 401-402. Proposition 6.1.

# Verification Notes

- Definition source: Direct quote from p. 401
- Confidence: HIGH — explicit definition
- Uncertainties: None
- Cross-reference status: Verified

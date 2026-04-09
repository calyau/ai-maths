---
# === CORE IDENTIFICATION ===
concept: Lie Algebra
slug: lie-algebra

# === CLASSIFICATION ===
category: lie-algebras
subcategory: definitions
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 24
section: "3.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathfrak{g}$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - commutator-bracket
  - jacobi-identity
extends: []
related:
  - lie-group
  - lie-algebra-morphism
  - lie-subalgebra
  - ideal-of-lie-algebra
  - lie-functor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

A Lie algebra is a vector space $\mathfrak{g}$ equipped with a bilinear map $[\,,\,]: \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ (the Lie bracket) that is skew-symmetric and satisfies the Jacobi identity.

# Core Definition

**Definition 3.16** (Kirillov): A Lie algebra is a vector space with a bilinear map $[\,,\,]: \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ which is skew-symmetric and satisfies Jacobi identity.

A morphism of Lie algebras is a linear map $f: \mathfrak{g}_1 \to \mathfrak{g}_2$ which preserves the commutator.

**Theorem 3.17**: For any Lie group $G$, $\mathfrak{g} = T_1G$ has a canonical Lie algebra structure; we write $\mathfrak{g} = \mathrm{Lie}(G)$. Every morphism of Lie groups induces a morphism of Lie algebras. For connected $G_1$, the map $\mathrm{Hom}(G_1, G_2) \to \mathrm{Hom}(\mathfrak{g}_1, \mathfrak{g}_2)$ is injective.

# Prerequisites

- **Commutator bracket** — provides the bracket operation
- **Jacobi identity** — the key axiom the bracket must satisfy

# Key Properties

1. Every Lie group $G$ determines a Lie algebra $\mathrm{Lie}(G) = T_1G$ (Theorem 3.17).
2. Every morphism of Lie groups $\varphi: G_1 \to G_2$ induces a Lie algebra morphism $\varphi_*: \mathfrak{g}_1 \to \mathfrak{g}_2$.
3. For connected $G_1$, the map on Hom sets is injective.
4. By Lie's third theorem: every finite-dimensional Lie algebra is the Lie algebra of some Lie group (Theorem 3.48).
5. The categories of finite-dimensional Lie algebras and connected simply-connected Lie groups are equivalent (Corollary 3.50).

# Construction / Recognition

## To Construct/Create:
1. Take $\mathfrak{g} = T_1G$ for a Lie group $G$.
2. Define $[x, y]$ via the commutator bracket (equation 3.2).
3. Alternatively, define abstractly: choose a vector space, define a bracket, verify skew-symmetry and Jacobi.

## To Identify/Recognize:
1. A vector space with a bilinear, skew-symmetric bracket satisfying the Jacobi identity.

# Context & Application

Lie algebras are linear objects that encode the essential structure of Lie groups. They are much easier to work with than groups — being vector spaces with a bilinear operation rather than manifolds with a nonlinear operation.

# Examples

**Example** (p. 23): $\mathfrak{gl}(n, \mathbb{K})$ with $[x, y] = xy - yx$.

**Example** (Section 3.10): $\mathfrak{so}(3, \mathbb{R})$ with $[J_x, J_y] = J_z$, $[J_y, J_z] = J_x$, $[J_z, J_x] = J_y$.

**Example** (p. 23): Any abelian group gives an abelian Lie algebra ($[x, y] = 0$).

# Relationships

## Builds Upon
- **Commutator bracket** — provides the bracket
- **Jacobi identity** — the axiom it must satisfy

## Enables
- **Lie subalgebra** — subalgebras of $\mathfrak{g}$
- **Ideal of Lie algebra** — special subalgebras
- **Center of Lie algebra** — $\mathfrak{z}(\mathfrak{g}) = \{x \mid [x, y] = 0\; \forall y\}$
- **Campbell-Hausdorff formula** — recovers the group law from the bracket
- **Fundamental theorems of Lie theory** — the algebra determines the group

## Related
- **Lie group** — every Lie algebra comes from a Lie group

# Common Errors

- **Error**: Assuming the Lie bracket is associative.
  **Correction**: Lie algebras are NOT associative in general. The Jacobi identity is the replacement.

# Common Confusions

- **Confusion**: Whether a Lie algebra determines a unique Lie group.
  **Clarification**: A Lie algebra determines a unique connected simply-connected Lie group. Other connected groups with the same algebra are quotients by discrete central subgroups (Corollary 3.49).

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.3, Definition 3.16, Theorem 3.17, page 24.

# Verification Notes

- Definition source: Direct from Definition 3.16
- Confidence rationale: Central explicit definition
- Uncertainties: None
- Cross-reference status: Verified with Theorem 3.17, Corollary 3.50

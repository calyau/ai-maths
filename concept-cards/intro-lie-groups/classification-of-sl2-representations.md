---
# === CORE IDENTIFICATION ===
concept: "Classification of Irreducible Representations of sl(2,C)"
slug: classification-of-sl2-representations

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of sl(2,C) and Spherical Laplace Operator"
chapter_number: 5
pdf_page: 60
section: "5.1 Representations of sl(2,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 5.6"
  - "irreducible reps of sl(2)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - highest-weight-for-sl2
  - highest-weight-vector-for-sl2
  - verma-module-for-sl2
  - weight-decomposition-for-sl2
extends: []
related:
  - integer-weights-for-sl2
  - weight-symmetry-for-sl2
  - irreducible-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does sl(2,C) serve as a building block for semisimple Lie algebras?"
  - "What are all the irreducible representations of sl(2,C)?"
  - "How do I decompose a representation into irreducibles?"
---

# Quick Definition

The irreducible finite-dimensional representations of $\mathfrak{sl}(2,\mathbb{C})$ are classified by non-negative integers: for each $n \geq 0$, there is exactly one irreducible representation $V_n$ of dimension $n+1$, with highest weight $n$ and weights $n, n-2, \ldots, -n$.

# Core Definition

**Theorem 5.6** (Kirillov, p. 60):

**(1)** For any $n \geq 0$, let $V_n$ be the $(n+1)$-dimensional vector space with basis $v^0, v^1, \ldots, v^n$. Define the action of $\mathfrak{sl}(2,\mathbb{C})$ by:

$$hv^k = (n - 2k)v^k$$
$$fv^k = (k+1)v^{k+1}, \quad k < n; \quad fv^n = 0$$
$$ev^k = (n+1-k)v^{k-1}, \quad k > 0; \quad ev^0 = 0$$

Then $V_n$ is an irreducible representation of $\mathfrak{sl}(2,\mathbb{C})$; it is called the irreducible representation with highest weight $n$.

**(2)** For $n \neq m$, the representations $V_n$ and $V_m$ are non-isomorphic.

**(3)** Every finite-dimensional irreducible representation of $\mathfrak{sl}(2,\mathbb{C})$ is isomorphic to one of the representations $V_n$.

# Prerequisites

- **Highest weight for sl(2,C)** — The classification is by highest weight
- **Highest weight vector for sl(2,C)** — The starting point for constructing $V_n$
- **Verma module for sl(2,C)** — $V_n$ is a quotient of $M^n$
- **Weight decomposition for sl(2,C)** — Underpins the proof

# Key Properties

1. $\dim V_n = n + 1$
2. Weights of $V_n$: $n, n-2, n-4, \ldots, -n+2, -n$ (each with multiplicity 1)
3. The highest weight $n$ is always a non-negative integer
4. $V_n$ can also be described as $S^n\mathbb{C}^2$, the $n$-th symmetric power of the standard representation (Exercise 5.2)
5. $V_0$ is the trivial representation, $V_1 = \mathbb{C}^2$ is the standard representation, $V_2$ is the adjoint representation
6. Non-isomorphism follows from $\dim V_n = n + 1$

# Construction / Recognition

## To Construct $V_n$:
1. Take $M^n$ (Verma module with $\lambda = n$)
2. The subspace spanned by $v^{n+1}, v^{n+2}, \ldots$ is a subrepresentation ($ev^{n+1} = 0$ when $\lambda = n$)
3. Quotient to get $V_n$ with basis $v^0, \ldots, v^n$

## Proof that Every Irreducible is $V_n$:
1. Let $V$ be irreducible with highest weight $\lambda$ and highest weight vector $v$
2. By Lemma 5.5, $V$ is a quotient of $M^\lambda$ spanned by $v^k = f^k v / k!$
3. Since $v^k$ have different weights, the nonzero ones are linearly independent
4. Let $n$ be maximal with $v^n \neq 0$, so $v^{n+1} = 0$
5. Then $ev^{n+1} = (\lambda - n)v^n = 0$, and since $v^n \neq 0$, we get $\lambda = n \in \mathbb{Z}_{\geq 0}$

# Context & Application

This is one of the most important results in the book. The classification of irreducible $\mathfrak{sl}(2,\mathbb{C})$-representations serves as the prototype for the classification of irreducible representations of all semisimple Lie algebras. The key features that generalize:
- Representations are classified by highest weights
- Highest weights must satisfy integrality conditions
- Each allowed highest weight gives exactly one irreducible
- Irreducible representations are constructed as quotients of Verma modules

In physics, these representations describe angular momentum multiplets: $V_n$ corresponds to spin $n/2$.

# Examples

**Example**: $V_0$: dimension 1, trivial representation. Weight: $\{0\}$.

**Example**: $V_1$: dimension 2, standard representation on $\mathbb{C}^2$. Weights: $\{1, -1\}$. This is the spin-$\frac{1}{2}$ representation.

**Example**: $V_2$: dimension 3, adjoint representation $\cong S^2\mathbb{C}^2 \cong \mathfrak{sl}(2,\mathbb{C})$. Weights: $\{2, 0, -2\}$. This is the spin-1 representation. $h \mapsto 2v^0$, $fv^0 = v^1$, $fv^1 = 2v^2$, $ev^1 = 2v^0$, $ev^2 = v^1$.

**Example**: $V_3$: dimension 4, $S^3\mathbb{C}^2$. Weights: $\{3, 1, -1, -3\}$. Spin-$\frac{3}{2}$.

# Relationships

## Builds Upon
- **Weight decomposition for sl(2,C)** — Foundation for the proof
- **Verma module for sl(2,C)** — Irreducibles are quotients
- **Highest weight vector** — Starting point of the construction

## Enables
- **Integer weights for sl(2,C)** — All weights are integers (corollary)
- **Weight symmetry** — $\dim V[n] = \dim V[-n]$ (corollary)
- **Spherical Laplace operator** — Applications to physics use this classification
- **Representation theory of semisimple algebras** — Generalization of this result

## Related
- **Irreducible representation** — These are the irreducible representations of $\mathfrak{sl}(2,\mathbb{C})$

# Common Errors

- **Error**: Confusing the highest weight $n$ with the dimension of $V_n$.
  **Correction**: The dimension is $n + 1$, not $n$. The irreducible with highest weight 2 has dimension 3.

- **Error**: Forgetting the factor $\frac{1}{k!}$ in $v^k = \frac{f^k}{k!}v$.
  **Correction**: The factorial normalization is essential for the clean formulas $fv^k = (k+1)v^{k+1}$ and $ev^k = (n+1-k)v^{k-1}$.

# Common Confusions

- **Confusion**: Thinking any complex number can be a highest weight.
  **Clarification**: For finite-dimensional representations, the highest weight must be a non-negative integer. This integrality condition is forced by the finite-dimensionality requirement ($ev^{n+1} = 0$ implies $\lambda = n$).

- **Confusion**: Believing the classification requires compact group theory.
  **Clarification**: The classification is purely algebraic, working directly with $\mathfrak{sl}(2,\mathbb{C})$. Compact group theory (complete reducibility) is used to show every representation decomposes into irreducibles, but the classification of irreducibles is independent.

# Source Reference

Chapter 5, Section 5.1, Theorem 5.6, pp. 60-61. This is the main theorem of Chapter 5.

# Verification Notes

- Definition source: Direct from Theorem 5.6, p. 60
- Confidence rationale: Complete theorem statement with full proof in the source
- Uncertainties: None
- Cross-reference status: Verified

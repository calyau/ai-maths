---
# === CORE IDENTIFICATION ===
concept: Trace Character
slug: trace-character

# === CLASSIFICATION ===
category: representations
subcategory: characters
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 48
section: "4.7 Orthogonality of characters and Peter-Weyl theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "group character"
  - "chi_V"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
  - matrix-coefficient
extends: []
related:
  - orthogonality-of-characters
  - multiplicity-formula
  - character-of-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compute the character of a representation?"
  - "What is the trace character of a group representation?"
---

# Quick Definition

The trace character of a representation $V$ of a group $G$ is the function $\chi_V(g) = \mathrm{tr}_V(\rho(g))$. It is basis-independent, conjugation-invariant, and detects isomorphism classes of completely reducible representations.

# Core Definition

**Definition 4.41** (Kirillov, p. 48): A character of a representation $V$ is the function on the group defined by

$$\chi_V(g) = \mathrm{tr}_V \rho(g) = \sum_i \rho_{ii}^V(g).$$

# Prerequisites

- **Representation of a Lie group** — The object whose character is computed
- **Matrix coefficient** — Characters are sums of diagonal matrix coefficients

# Key Properties

**Lemma 4.42** (p. 48):
1. Trivial representation: $\chi_{\mathbb{C}} = 1$
2. Direct sum: $\chi_{V \oplus W} = \chi_V + \chi_W$
3. Tensor product: $\chi_{V \otimes W} = \chi_V \cdot \chi_W$
4. Conjugation invariance: $\chi_V(ghg^{-1}) = \chi_V(h)$ (class function)
5. Dual: $\chi_{V^*} = \overline{\chi_V}$
6. Characters of irreducibles form an orthonormal set (Theorem 4.43)
7. $V$ is irreducible iff $(\chi_V, \chi_V) = 1$ (Corollary 4.44)
8. Multiplicities: $N_i = (\chi_V, \chi_{V_i})$ (Corollary 4.44)

# Construction / Recognition

## To Compute:
1. Choose any basis of $V$
2. Compute $\rho(g)$ as a matrix
3. Take the trace: $\chi_V(g) = \sum_i \rho_{ii}(g)$
4. The result is independent of basis choice

# Context & Application

The trace character is the primary tool for decomposing representations of compact groups. For $G = S^1$, characters are Fourier exponentials and the theory reduces to Fourier analysis. The trace character is related to but distinct from the formal character (Chapter 9), which is an element of the group ring of the weight lattice.

# Examples

**Example 4.49** (p. 50): For $G = S^1$, the character of $V_k$ is $\chi_k(a) = e^{2\pi ika}$. Orthogonality gives $\int_0^1 e^{2\pi ikx}\overline{e^{2\pi ilx}}\, dx = \delta_{kl}$.

# Relationships

## Builds Upon
- **Matrix coefficient** — Characters are traces of matrix coefficients

## Enables
- **Orthogonality of characters** — Key structural result
- **Multiplicity formula** — $N_i = (\chi_V, \chi_{V_i})$
- **Irreducibility criterion** — $(\chi_V, \chi_V) = 1$

## Related
- **Character of representation** — The formal character (Chapter 9) is the weight-lattice version

# Common Confusions

- **Confusion**: Confusing the trace character $\chi_V(g) = \mathrm{tr}(\rho(g))$ with the formal character $\mathrm{ch}(V) = \sum (\dim V[\lambda]) e^\lambda$.
  **Clarification**: The trace character is a function on the group; the formal character is an element of $\mathbb{Z}[P]$. They encode the same information but in different forms.

# Source Reference

Chapter 4, Section 4.7, Definition 4.41, Lemma 4.42, Theorem 4.43, Corollary 4.44, pp. 48-49.

# Verification Notes

- Definition source: Direct from Definition 4.41, p. 48
- Confidence rationale: Explicit definition with complete properties
- Uncertainties: None
- Cross-reference status: Verified

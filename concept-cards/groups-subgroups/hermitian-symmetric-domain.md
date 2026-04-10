---
# === CORE IDENTIFICATION ===
concept: Hermitian Symmetric Domain
slug: hermitian-symmetric-domain

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
pdf_page: 411
section: "Shimura varieties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - bounded symmetric domain

# === TYPED RELATIONSHIPS ===
prerequisites:
  - reductive-algebraic-group
  - lie-group
extends: []
related:
  - connected-shimura-variety
  - fundamental-domain-sl2
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Shimura variety?"
---

# Quick Definition

A hermitian symmetric domain is a complex manifold of the form $X = G(\mathbb{R})^+/K$ where $G$ is a semisimple adjoint group over $\mathbb{R}$ and $K$ is a maximal compact subgroup determined by a homomorphism $u: U_1 \to G(\mathbb{R})$ satisfying specific conditions. The upper half-plane $\mathcal{H}$ is the simplest example.

# Core Definition

Theorem 16.1 (Milne, p. 411): Let $G$ be a semisimple adjoint group over $\mathbb{R}$, and let $u: U_1 \to G(\mathbb{R})$ be a homomorphism such that:

(a) Only the characters $z^{-1}$, $1$, $z$ occur in the representation of $U_1$ on $\mathrm{Lie}(G)_{\mathbb{C}}$;

(b) $K_{\mathbb{C}} = \{g \in G(\mathbb{C}) \mid g = \mathrm{inn}(u(-1))(\bar{g})\}$ is compact;

(c) $u(-1)$ does not project to $1$ in any simple factor of $G$.

Then $K = K_{\mathbb{C}} \cap G(\mathbb{R})^+$ is a maximal compact subgroup of $G(\mathbb{R})^+$, and there is a unique structure of a complex manifold on $X = G(\mathbb{R})^+/K$ such that $G(\mathbb{R})^+$ acts by holomorphic maps. The complex manifolds arising in this way are the *hermitian symmetric domains*.

# Prerequisites

- **Reductive algebraic group** — $G$ is a semisimple adjoint group
- **Lie group** — $G(\mathbb{R})$ is a real Lie group

# Key Properties

1. Hermitian symmetric domains are complex manifolds, not algebraic varieties
2. They carry a unique complex structure compatible with the group action
3. $u(z)$ acts on the tangent space at $p = 1K$ as multiplication by $z$
4. The upper half-plane $\mathcal{H} \simeq \mathrm{SL}_2(\mathbb{R})/\mathrm{SO}(2)$ is the simplest example
5. Certain quotients of hermitian symmetric domains by arithmetic subgroups are algebraic varieties (Baily-Borel)

# Construction / Recognition

## To Construct:
1. Choose a semisimple adjoint group $G$ over $\mathbb{R}$
2. Find a homomorphism $u: U_1 \to G(\mathbb{R})$ satisfying conditions (a)-(c)
3. The hermitian symmetric domain is $X = G(\mathbb{R})^+/K$

# Context & Application

Hermitian symmetric domains are the "upstairs" spaces for Shimura varieties. While not algebraic themselves, their quotients by congruence subgroups acquire canonical algebraic structures (Baily-Borel theorem) and canonical models over number fields.

# Examples

**Example 1** (p. 411): For $G = \mathrm{SL}_2/\{\pm I\} = \mathrm{PGL}_2$, define $u$ by mapping $z \in U_1$ to $\begin{pmatrix}a & b \\ -b & a\end{pmatrix}$ where $a + ib = \sqrt{z}$. Then $K = \mathrm{SO}(2)$ and $X = \mathrm{SL}_2(\mathbb{R})/\mathrm{SO}(2) \simeq \mathcal{H}$, the upper half-plane.

# Relationships

## Enables
- **Connected Shimura variety** — quotients of hermitian symmetric domains by congruence subgroups

## Related
- **Fundamental domain for SL₂** — $\mathcal{H}$ is the simplest hermitian symmetric domain

# Common Errors

- **Error**: Thinking hermitian symmetric domains are algebraic varieties
  **Correction**: They are complex manifolds; they become algebraic only after taking quotients by arithmetic subgroups

# Common Confusions

- **Confusion**: Confusing a hermitian symmetric domain with a hermitian symmetric space
  **Clarification**: Hermitian symmetric domains are the noncompact type; compact hermitian symmetric spaces are different (and are projective varieties)

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 16, pages 411-412. Theorem 16.1.

# Verification Notes

- Definition source: Theorem 16.1 directly from p. 411
- Confidence: HIGH — explicit theorem with conditions
- Uncertainties: Proof references Helgason 1978 and Milne 2005
- Cross-reference status: Verified

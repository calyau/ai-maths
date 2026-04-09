---
# === CORE IDENTIFICATION ===
concept: Structure Theorem for Roots
slug: structure-theorem-roots

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 87
section: "7.3. Root decomposition and root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 7.21"
  - "main theorem on root structure"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-decomposition
  - sl2-subalgebra-of-root
extends:
  - root-decomposition
related:
  - root-system-axioms
  - root-string
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the key structural properties of roots in a semisimple Lie algebra?"
---

# Quick Definition

Theorem 7.21 establishes the seven fundamental properties of the root system: roots span $\mathfrak{h}^*$, root spaces are one-dimensional, the numbers $\langle h_\alpha, \beta \rangle$ are integers, reflections $s_\alpha$ preserve the root system, the only multiples of a root that are roots are $\pm\alpha$, root strings are irreducible $\mathfrak{sl}(2)$ representations, and brackets of root spaces are surjective when the sum is a root.

# Core Definition

**Theorem 7.21** (Kirillov, p. 87): Let $\mathfrak{g}$ be complex semisimple with Cartan subalgebra $\mathfrak{h}$.
1. $R$ spans $\mathfrak{h}^*$; $h_\alpha$ ($\alpha \in R$) span $\mathfrak{h}$
2. $\dim \mathfrak{g}_\alpha = 1$ for each $\alpha \in R$
3. $\langle h_\alpha, \beta \rangle = \frac{2(\alpha, \beta)}{(\alpha, \alpha)} \in \mathbb{Z}$ for all $\alpha, \beta \in R$
4. $s_\alpha(\beta) = \beta - \langle h_\alpha, \beta \rangle \alpha \in R$ for all $\alpha, \beta \in R$
5. If $\alpha \in R$, the only multiples of $\alpha$ in $R$ are $\pm\alpha$
6. For $\beta \neq \pm\alpha$, $\bigoplus_{k \in \mathbb{Z}} \mathfrak{g}_{\beta+k\alpha}$ is irreducible under $\mathfrak{sl}(2, \mathbb{C})_\alpha$
7. If $\alpha, \beta, \alpha + \beta \in R$, then $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] = \mathfrak{g}_{\alpha+\beta}$

# Prerequisites

- **Root decomposition** — The setting for the theorem
- **sl(2) subalgebra of a root** — The key tool for all proofs

# Key Properties

1. Part (1): If roots don't span, some $h$ has $\langle h, \alpha \rangle = 0$ for all $\alpha$, so $\operatorname{ad} h = 0$, contradicting $\mathfrak{z}(\mathfrak{g}) = 0$
2. Part (2): Follows from irreducibility of $V = \mathbb{C}h_\alpha \oplus \bigoplus_{k \neq 0} \mathfrak{g}_{k\alpha}$ (Lemma 7.20)
3. Part (3): Weights of $\mathfrak{sl}(2)$ representations are integers
4. Part (4): Reflection by $f_\alpha^n$ maps weight $n$ to weight $-n$
5. Part (5): $2\alpha$ is never a root (from the irreducible $\mathfrak{sl}(2)$ representation structure)
6. Part (7): Follows from the nonvanishing of $e$ action in $\mathfrak{sl}(2)$ representations

# Context & Application

This is the culminating theorem of Chapter 7. It shows that the root system of a semisimple Lie algebra satisfies all the axioms of an abstract root system, establishing the bridge to the combinatorial classification theory of Chapter 8.

# Examples

**Example**: For $\mathfrak{sl}(3, \mathbb{C})$: roots are $\pm(e_1 - e_2), \pm(e_1 - e_3), \pm(e_2 - e_3)$. Each root space is 1-dimensional. The number $\langle h_{e_1-e_2}, e_1-e_3 \rangle = 1 \in \mathbb{Z}$.

# Relationships

## Builds Upon
- **sl(2) subalgebra** — All proofs use $\mathfrak{sl}(2, \mathbb{C})_\alpha$ representations

## Enables
- **Root system axioms** — Proves the root system satisfies the abstract axioms
- **Classification of semisimple algebras** — Via the root system

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, pages 87-89. Theorem 7.21.

# Verification Notes

- Definition source: Direct from Theorem 7.21
- Confidence rationale: Major theorem with all seven parts proved
- Uncertainties: None
- Cross-reference status: Verified

---
# === CORE IDENTIFICATION ===
concept: Semisimple Lie Algebra
slug: semisimple-lie-algebra

# === CLASSIFICATION ===
category: structure-theory
subcategory: semisimple
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 71
section: "6.4. The radical. Semisimple and reductive algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-lie-algebra
  - lie-algebra-ideal
extends: []
related:
  - simple-lie-algebra
  - radical
  - reductive-lie-algebra
  - killing-form
  - cartan-criterion-semisimplicity
contrasts_with:
  - solvable-lie-algebra
  - reductive-lie-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a semisimple Lie algebra?"
  - "How do I determine if a Lie algebra is semisimple?"
  - "What distinguishes a semisimple Lie algebra from a reductive one?"
---

# Quick Definition

A semisimple Lie algebra is one that contains no nonzero solvable ideals, or equivalently, one whose Killing form is non-degenerate. Semisimple algebras decompose as direct sums of simple algebras and form the "opposite extreme" from solvable algebras.

# Core Definition

**Definition 6.19** (Kirillov, p. 71): A Lie algebra $\mathfrak{g}$ is called semisimple if it contains no nonzero solvable ideals.

Equivalently (Theorem 6.37, Cartan criterion): $\mathfrak{g}$ is semisimple iff the Killing form $K(x,y) = \operatorname{tr}(\operatorname{ad} x \cdot \operatorname{ad} y)$ is non-degenerate.

Equivalently: $\mathfrak{g}$ is semisimple iff $\operatorname{rad}(\mathfrak{g}) = 0$.

# Prerequisites

- **Solvable Lie algebra** — Semisimplicity is defined as absence of solvable ideals
- **Lie algebra ideal** — The definition involves ideals

# Key Properties

1. The center $\mathfrak{z}(\mathfrak{g}) = 0$ for any semisimple algebra
2. $[\mathfrak{g}, \mathfrak{g}] = \mathfrak{g}$ (Corollary 6.44)
3. Every ideal in a semisimple algebra has a complementary ideal (Theorem 6.42)
4. A semisimple algebra is a direct sum of simple algebras (Corollary 6.43)
5. Every representation is completely reducible (Theorem 6.57)
6. Every derivation is inner: $\operatorname{Der} \mathfrak{g} = \mathfrak{g}$ (Proposition 6.47)
7. $\mathfrak{g}$ is semisimple iff $\mathfrak{g}^{\mathbb{C}}$ is semisimple (Proposition 6.40)

# Construction / Recognition

## To Identify/Recognize:
1. Compute the Killing form $K(x,y) = \operatorname{tr}(\operatorname{ad} x \cdot \operatorname{ad} y)$
2. Check if $K$ is non-degenerate (Cartan criterion)
3. Alternatively, check $\operatorname{rad}(\mathfrak{g}) = 0$

## Known Semisimple Algebras:
- $\mathfrak{sl}(n, \mathbb{K})$, $\mathfrak{so}(n, \mathbb{K})$ ($n > 2$), $\mathfrak{su}(n)$, $\mathfrak{sp}(2n, \mathbb{K})$ (Theorem 6.33)

# Context & Application

Semisimple Lie algebras are the central objects of the classification theory. Every Lie algebra decomposes (via Levi decomposition) into a solvable radical and a semisimple part. The semisimple part is fully classified by root systems and Dynkin diagrams. The representation theory of semisimple algebras is completely controlled by the root decomposition.

# Examples

**Example 6.22** (p. 71): $\mathfrak{sl}(2, \mathbb{C})$ is simple (hence semisimple). The proof uses the fact that $\operatorname{ad} h$ is diagonal with distinct eigenvalues $2, -2, 0$, so any ideal must be spanned by a subset of $\{e, f, h\}$, and any nonzero choice generates all of $\mathfrak{sl}(2, \mathbb{C})$.

**Theorem 6.33** (p. 74): Classical algebras $\mathfrak{sl}(n)$, $\mathfrak{so}(n)$ ($n > 2$), $\mathfrak{su}(n)$, $\mathfrak{sp}(2n)$ are all semisimple, proved via non-degeneracy of the trace form.

# Relationships

## Builds Upon
- **Solvable Lie algebra** — Defined as absence of solvable ideals

## Enables
- **Root decomposition** — The fundamental structural tool for semisimple algebras
- **Cartan subalgebra** — Exists in every semisimple algebra
- **Complete reducibility** — All representations are completely reducible

## Related
- **Simple Lie algebra** — Building blocks of semisimple algebras
- **Killing form** — Non-degeneracy characterizes semisimplicity

## Contrasts With
- **Solvable Lie algebra** — The opposite extreme; no nonzero solvable ideals
- **Reductive Lie algebra** — Allows a center; semisimple means reductive with zero center

# Common Errors

- **Error**: Assuming semisimple means simple
  **Correction**: Semisimple algebras can be direct sums of multiple simple algebras

# Common Confusions

- **Confusion**: Confusing semisimple Lie algebra with semisimple operator
  **Clarification**: A semisimple algebra has no solvable ideals; a semisimple operator is diagonalizable. The terminological overlap reflects a deeper connection via the Jordan decomposition in semisimple algebras.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.4, pages 71-72. Definition 6.19, Example 6.22, Theorem 6.33, Theorem 6.37.

# Verification Notes

- Definition source: Direct from Definition 6.19
- Confidence rationale: Central definition of the chapter with multiple characterizations
- Uncertainties: None
- Cross-reference status: Verified

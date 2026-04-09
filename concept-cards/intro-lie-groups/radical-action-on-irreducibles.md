---
# === CORE IDENTIFICATION ===
concept: Radical Action on Irreducible Representations
slug: radical-action-on-irreducibles

# === CLASSIFICATION ===
category: structure-theory
subcategory: semisimple
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 72
section: "6.4. The radical. Semisimple and reductive algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - radical
  - representation-lie-algebra
  - lie-theorem
extends:
  - lie-theorem
related:
  - reductive-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the radical act in irreducible representations?"
---

# Quick Definition

In any irreducible representation of a Lie algebra $\mathfrak{g}$, elements of $\operatorname{rad}(\mathfrak{g})$ act by scalar operators, and elements of $[\mathfrak{g}, \operatorname{rad}(\mathfrak{g})]$ act by zero. This motivates the definitions of semisimple and reductive algebras.

# Core Definition

**Theorem 6.27** (Kirillov, p. 72): Let $V$ be an irreducible representation of $\mathfrak{g}$. Then any $h \in \operatorname{rad}(\mathfrak{g})$ acts in $V$ by scalar operators: $\rho(h) = \lambda(h) \operatorname{id}$. Also, any $h \in [\mathfrak{g}, \operatorname{rad}(\mathfrak{g})]$ acts by zero.

# Prerequisites

- **Radical** — The theorem describes how the radical acts
- **Representation of a Lie algebra** — The setting is an irreducible representation
- **Lie theorem** — The proof uses Proposition 6.15 (common eigenvector)

# Key Properties

1. The eigenvalue $\lambda$ defines a linear functional $\lambda\colon \operatorname{rad}(\mathfrak{g}) \to \mathbb{C}$
2. The common eigenspace $V^\lambda$ is a subrepresentation, hence equals $V$ by irreducibility
3. Elements in $[\mathfrak{g}, \operatorname{rad}(\mathfrak{g})]$ necessarily act by zero (scalar commutators vanish)

# Context & Application

This theorem explains why having a nonzero $[\mathfrak{g}, \operatorname{rad}(\mathfrak{g})]$ complicates representation theory: it produces elements acting by zero in every irreducible representation. This motivates the definition of reductive algebras ($[\mathfrak{g}, \operatorname{rad}(\mathfrak{g})] = 0$).

# Examples

**Example**: For $\mathfrak{gl}(n) = \mathbb{C} \cdot \operatorname{id} \oplus \mathfrak{sl}(n)$, the radical is $\mathbb{C} \cdot \operatorname{id}$ (the center). In any irreducible representation, $\operatorname{id}$ acts by a scalar (Schur's lemma), consistent with the theorem. Since $[\mathfrak{gl}(n), \mathbb{C} \cdot \operatorname{id}] = 0$, $\mathfrak{gl}(n)$ is reductive.

# Relationships

## Builds Upon
- **Lie theorem** — Uses common eigenvector result

## Enables
- **Reductive Lie algebra** — Motivates the definition

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.4, page 72. Theorem 6.27.

# Verification Notes

- Definition source: Direct from Theorem 6.27
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified

---
# === CORE IDENTIFICATION ===
concept: Positive Root Cone Q+
slug: q-plus-cone

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Semisimple Lie Algebras"
chapter_number: 9
pdf_page: 112
section: "9.2 Highest-weight representations and Verma modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Q_+"
  - "positive root cone"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots
  - root-lattice
extends: []
related:
  - verma-module
  - weight-set
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Q+?"
  - "How are the weights of a highest-weight module constrained?"
---

# Quick Definition
$Q_+ = \{\sum n_i \alpha_i \mid n_i \in \mathbb{Z}_+\}$ is the set of non-negative integer combinations of simple roots. Weights of a highest-weight module with highest weight $\lambda$ lie in $\lambda - Q_+$.

# Core Definition
(Kirillov, p. 112, Theorem 9.9): The positive root cone is $Q_+ = \{\sum n_i \alpha_i \mid n_i \in \mathbb{Z}_+\}$ where $\alpha_1, \ldots, \alpha_r$ are the simple roots. The weight set of the Verma module satisfies $P(M_\lambda) = \lambda - Q_+$.

# Prerequisites
- **Simple roots** -- the generators $\alpha_1, \ldots, \alpha_r$
- **Root lattice** -- $Q_+ \subset Q$

# Key Properties
1. $Q_+$ is the "positive cone" of the root lattice $Q$
2. $Q_+ \cap (-Q_+) = \{0\}$, defining a partial order on $\mathfrak{h}^*$
3. $P(M_\lambda) = \lambda - Q_+$ for Verma modules
4. $P(V) \subset \lambda - Q_+$ for any highest-weight module with highest weight $\lambda$

# Context & Application
The cone $Q_+$ defines the natural partial order on weights: $\mu \leq \lambda$ iff $\lambda - \mu \in Q_+$. This partial order is fundamental to the theory of highest-weight modules: all weights of a highest-weight module lie at or below the highest weight.

# Examples
**Example**: For $\mathfrak{sl}(2, \mathbb{C})$, $Q_+ = \{n\alpha \mid n \in \mathbb{Z}_+\} = 2\mathbb{Z}_+$, so weights of $M_\lambda$ are $\lambda, \lambda - 2, \lambda - 4, \ldots$.

# Relationships
## Builds Upon
- **Simple roots** -- generate $Q_+$

## Enables
- **Verma module** -- weight set is $\lambda - Q_+$
- **Partial order on weights** -- defined by $Q_+$

# Source Reference
Chapter 9, Section 9.2, Theorem 9.9(2) and Theorem 9.10(2), pp. 112-113.

# Verification Notes
- Definition source: Direct from Theorem 9.9
- Confidence rationale: Explicitly defined in theorem
- Uncertainties: None
- Cross-reference status: Verified

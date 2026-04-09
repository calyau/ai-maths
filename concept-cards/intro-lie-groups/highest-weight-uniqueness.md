---
# === CORE IDENTIFICATION ===
concept: Uniqueness of Highest Weight
slug: highest-weight-uniqueness

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Semisimple Lie Algebras"
chapter_number: 9
pdf_page: 113
section: "9.2 Highest-weight representations and Verma modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Corollary 9.12"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - highest-weight-representation
  - verma-module-basis
extends: []
related:
  - highest-weight-vector
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is the highest weight of a highest-weight module unique?"
  - "Can a highest-weight module have multiple highest-weight vectors?"
---

# Quick Definition
In any highest-weight module, the highest weight is unique and the highest-weight vector is unique up to a scalar multiple. This follows from the fact that all weights lie in $\lambda - Q_+$.

# Core Definition
**Corollary 9.12** (Kirillov, p. 113): In any highest weight module, there is a unique highest weight and unique up to a scalar highest weight vector.

**Proof**: If $\lambda, \mu$ are both highest weights, then $\lambda - \mu \in Q_+$ and $\mu - \lambda \in Q_+$ (by Theorem 9.10(2)), which forces $\lambda = \mu$. Uniqueness of the vector follows from $\dim V[\lambda] = 1$.

# Prerequisites
- **Highest-weight representation** -- the module in question
- **Verma module basis** -- provides $P(V) \subset \lambda - Q_+$

# Key Properties
1. The highest weight $\lambda$ is uniquely determined
2. The highest-weight vector is unique up to scalar
3. The proof uses the partial order: if $\lambda - \mu \in Q_+$ and $\mu - \lambda \in Q_+$, then $\lambda = \mu$

# Context & Application
This corollary justifies speaking of "the" highest weight of a highest-weight module. It ensures that the classification of irreducible representations by their highest weight is well-defined.

# Examples
**Example** (p. 113): The argument shows that no two distinct elements of $P(V)$ can satisfy both $\lambda - \mu \in Q_+$ and $\mu - \lambda \in Q_+$.

# Relationships
## Builds Upon
- **Highest-weight representation** -- the concept being clarified

## Enables
- **Classification of irreducible representations** -- uniqueness makes the classification well-defined

# Source Reference
Chapter 9, Section 9.2, Corollary 9.12, p. 113.

# Verification Notes
- Definition source: Direct from Corollary 9.12
- Confidence rationale: Explicit corollary with proof
- Uncertainties: None
- Cross-reference status: Verified

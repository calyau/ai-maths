---
# === CORE IDENTIFICATION ===
concept: Reduced Root System
slug: reduced-root-system

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 90
section: "8.1. Abstract root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
  - root-system-axioms
extends:
  - abstract-root-system
related:
  - reducible-root-system
contrasts_with:
  - abstract-root-system

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a reduced root system?"
  - "What additional condition distinguishes reduced from non-reduced root systems?"
---

# Quick Definition
A reduced root system is a root system satisfying the additional axiom (R4): if $\alpha$ and $c\alpha$ are both roots, then $c = \pm 1$. Equivalently, no root is a nontrivial positive scalar multiple of another root.

# Core Definition
A root system $R$ is called reduced if it satisfies axiom (R4): if $\alpha, c\alpha \in R$, then $c = \pm 1$ (Definition 8.1, p. 90). This rules out the possibility that both $\alpha$ and $2\alpha$ (or $\alpha/2$) belong to $R$.

# Prerequisites
- **abstract-root-system** -- a reduced root system is an abstract root system with an extra axiom
- **root-system-axioms** -- axiom R4 is added to axioms R1--R3

# Key Properties
1. Every pair of proportional roots consists only of $\alpha$ and $-\alpha$
2. Axiom R4 does not follow from R1--R3 (Remark 8.2, p. 91)
3. The root system of any semisimple complex Lie algebra is reduced (Theorem 8.3)
4. The classification theorem (Theorem 8.49) classifies reduced irreducible root systems

# Construction / Recognition
## To check reducedness
1. For each root $\alpha \in R$, check whether $2\alpha \in R$
2. If no root has its double also in $R$, the system is reduced

# Context & Application
Most of the theory in Chapter 8 concerns reduced root systems. The classification of Dynkin diagrams (Theorem 8.49) applies specifically to reduced irreducible root systems. The root systems arising from semisimple Lie algebras are always reduced.

# Examples
**Example** (p. 91): The root system $A_{n-1} = \{e_i - e_j \mid i \neq j\}$ is reduced since all roots have the same length $\sqrt{2}$, so no root can be a scalar multiple of another (apart from $\pm 1$).

**Counterexample** (Exercise 8.1, p. 108): The root system $BC_n = \{\pm e_i, \pm 2e_i\} \cup \{\pm e_i \pm e_j \mid i \neq j\}$ is non-reduced because it contains both $e_i$ and $2e_i$.

# Relationships
## Builds Upon
- **abstract-root-system** -- adds axiom R4

## Enables
- **simple-roots** -- the theory of positive and simple roots is developed for reduced systems
- **dynkin-diagram** -- classification applies to reduced irreducible root systems

## Related
- **reducible-root-system** -- orthogonal decomposability (unrelated to reducedness)

## Contrasts With
- **abstract-root-system** -- which may be non-reduced

# Common Errors
- **Error**: Assuming all root systems are reduced
  **Correction**: Non-reduced root systems such as $BC_n$ exist and satisfy R1--R3 but not R4

# Common Confusions
- **Confusion**: Conflating "reduced" with "irreducible"
  **Clarification**: "Reduced" means no proportional roots beyond $\pm\alpha$; "irreducible" means not decomposable as an orthogonal union. These are completely independent properties (Remark 8.41, p. 103)

# Source Reference
Chapter 8: Root Systems, Section 8.1, pages 90--91. Definition 8.1 (R4), Remark 8.2, Remark 8.41.

# Verification Notes
- Definition source: Direct from Definition 8.1
- Confidence rationale: HIGH -- explicit axiom with explicit remark about independence
- Uncertainties: None
- Cross-reference status: Verified

---
# === CORE IDENTIFICATION ===
concept: Root System Axioms
slug: root-system-axioms

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
aliases:
  - "axioms R1-R4"
  - "root system conditions"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - abstract-root-system
  - reflection-in-root-system
  - reduced-root-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the four axioms of a root system?"
  - "What does each root system axiom mean geometrically?"
---

# Quick Definition
The root system axioms are four conditions (R1--R4) that a finite set of vectors must satisfy to be a (reduced) root system: spanning, integrality of projections, closure under reflections, and non-proportionality.

# Core Definition
Given a real vector space $E$ with positive definite inner product and a finite set $R \subset E \setminus \{0\}$, the axioms are (Definition 8.1, p. 90):

- **(R1)** $R$ generates $E$ as a vector space.
- **(R2)** For any $\alpha, \beta \in R$, the number $n_{\alpha\beta} = \frac{2(\alpha,\beta)}{(\beta,\beta)}$ is an integer.
- **(R3)** For any $\alpha, \beta \in R$, $s_\alpha(\beta) \in R$, where $s_\alpha(\lambda) = \lambda - \frac{2(\alpha,\lambda)}{(\alpha,\alpha)}\alpha$.
- **(R4)** If $\alpha, c\alpha \in R$, then $c = \pm 1$.

Axioms R1--R3 define a root system; adding R4 gives a reduced root system.

# Prerequisites
This is a foundational concept. Understanding requires:
- **Inner product** -- used in the integrality condition (R2) and reflection formula (R3)
- **Reflection** -- the geometric operation $s_\alpha$ in axiom (R3)

# Key Properties
1. **(R1) Spanning**: $R$ spans all of $E$, ensuring the root system has no "wasted" dimensions
2. **(R2) Integrality**: The projection of any root $\alpha$ onto the line through $\beta$ is a half-integer multiple of $\beta$; equivalently $p_\alpha(\beta) = \frac{n_{\beta\alpha}}{2}\alpha$ (p. 91)
3. **(R3) Reflection closure**: $R$ is invariant under every reflection $s_\alpha$, $\alpha \in R$
4. **(R4) Reducedness**: No root is a nontrivial scalar multiple of another; this does not follow from R1--R3 (Remark 8.2)
5. From R1--R3 alone, if $\alpha$ and $c\alpha$ are both roots, then $c \in \{\pm 1, \pm 2, \pm 1/2\}$

# Construction / Recognition
## To check each axiom
1. **(R1)**: Verify that $\operatorname{span}(R) = E$
2. **(R2)**: For each pair $\alpha,\beta$, compute $2(\alpha,\beta)/(\beta,\beta)$ and check it is in $\mathbb{Z}$
3. **(R3)**: For each pair, compute $s_\alpha(\beta) = \beta - n_{\beta\alpha}\,\alpha$ and verify $s_\alpha(\beta) \in R$
4. **(R4)**: Check that no two roots are positive scalar multiples of each other (other than $\alpha$ and $-\alpha$)

# Context & Application
These axioms distill the properties of root systems of semisimple Lie algebras (Theorem 8.3) into a self-contained combinatorial framework. The integrality axiom (R2) is the most restrictive and is responsible for the eventual finite classification of root systems.

# Examples
**Example** (p. 91): For $A_{n-1}$, with $R = \{e_i - e_j \mid i \neq j\} \subset E$, axiom (R2) follows from $(\alpha,\alpha) = 2$ for all $\alpha \in R$ so $n_{\alpha\beta} = (\alpha,\beta) \in \mathbb{Z}$. Axiom (R3) holds because the reflections act as transpositions of coordinates, which permute $R$. Axiom (R4) is immediate since all roots have equal length.

# Relationships
## Builds Upon
- Euclidean geometry, inner products

## Enables
- **abstract-root-system** -- defined by these axioms
- **reduced-root-system** -- defined by R1--R4

## Related
- **reflection-in-root-system** -- the operation appearing in R3
- **coroot** -- reformulates R2 as $\langle\alpha^\vee, \beta\rangle \in \mathbb{Z}$

## Contrasts With
(none)

# Common Errors
- **Error**: Checking only R2 or only R3, assuming the other follows
  **Correction**: R2 and R3 are independent conditions; both must be verified separately

# Common Confusions
- **Confusion**: Thinking R4 follows from R1--R3
  **Clarification**: It does not; the $BC_n$ root system satisfies R1--R3 but not R4 (Remark 8.2, Exercise 8.1)

# Source Reference
Chapter 8: Root Systems, Section 8.1, pages 90--91. Definition 8.1, Remark 8.2.

# Verification Notes
- Definition source: Direct from Definition 8.1
- Confidence rationale: HIGH -- explicit numbered axioms in source
- Uncertainties: None
- Cross-reference status: Verified

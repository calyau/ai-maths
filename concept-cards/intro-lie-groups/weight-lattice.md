---
# === CORE IDENTIFICATION ===
concept: Weight Lattice
slug: weight-lattice

# === CLASSIFICATION ===
category: root-systems
subcategory: lattices
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 97
section: "8.5. Weight and root lattices"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$P$"
  - "integral weights"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - coroot
  - coroot-lattice
extends: []
related:
  - root-lattice
  - fundamental-weights
  - quotient-p-mod-q
contrasts_with:
  - root-lattice

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the weight lattice?"
  - "What distinguishes the weight lattice from the root lattice?"
---

# Quick Definition
The weight lattice $P$ consists of all $\lambda \in E$ with $\langle\lambda,\alpha^\vee\rangle \in \mathbb{Z}$ for every root $\alpha$. It is the dual lattice of the coroot lattice $Q^\vee$ and contains the root lattice $Q$ as a sublattice.

# Core Definition
The weight lattice is defined by (equation 8.12, p. 97):

$$P = \{\lambda \in E \mid \langle\lambda,\alpha^\vee\rangle \in \mathbb{Z} \text{ for all } \alpha \in R\}$$

Elements of $P$ are called integral weights. Since $Q^\vee = \bigoplus\mathbb{Z}\alpha_i^\vee$, equivalently (equation 8.13):

$$P = \{\lambda \in E \mid \langle\lambda,\alpha_i^\vee\rangle \in \mathbb{Z} \text{ for all simple } \alpha_i\}$$

The weight lattice equals $P = \bigoplus_i \mathbb{Z}\omega_i$, where $\omega_i$ are the fundamental weights.

# Prerequisites
- **coroot** -- used in the definition $\langle\lambda,\alpha^\vee\rangle \in \mathbb{Z}$
- **coroot-lattice** -- $P$ is the dual lattice of $Q^\vee$

# Key Properties
1. $P = \bigoplus_{i=1}^r \mathbb{Z}\omega_i$ where $\omega_i$ are fundamental weights
2. $Q \subset P$ (since $n_{\alpha\beta} \in \mathbb{Z}$ implies roots are integral weights)
3. $P/Q$ is a finite abelian group with $|P/Q| = |\det A|$ (Exercise 8.4)
4. $P$ is the dual lattice of $Q^\vee$

# Construction / Recognition
1. Compute simple coroots $\alpha_i^\vee$
2. Define fundamental weights $\omega_i$ by $\langle\omega_i,\alpha_j^\vee\rangle = \delta_{ij}$
3. $P = \bigoplus \mathbb{Z}\omega_i$

# Context & Application
The weight lattice is central to representation theory (Chapter 9). Weights of finite-dimensional representations of a semisimple Lie algebra lie in $P$. The quotient $P/Q$ is isomorphic to the center of the simply-connected Lie group with the given root system.

# Examples
**Example 8.20** (p. 97): For $A_1$, $\omega = \alpha/2$, so $P = \mathbb{Z}(\alpha/2)$ and $P/Q = \mathbb{Z}_2$.

**Example 8.21** (p. 97): For $A_2$, the weight and root lattices are shown in Figure 8.3. Bold dots are $Q$; open dots are $P \setminus Q$. One has $P/Q = \mathbb{Z}_3$.

# Relationships
## Builds Upon
- **coroot-lattice** -- $P$ is its dual lattice
- **fundamental-weights** -- provide a $\mathbb{Z}$-basis of $P$

## Enables
- **quotient-p-mod-q** -- $P/Q$ is a fundamental invariant

## Related
- **root-lattice** -- a sublattice of $P$

## Contrasts With
- **root-lattice** -- $Q$ is (usually) a proper sublattice of $P$

# Common Errors
- **Error**: Thinking the weight lattice and root lattice are always equal
  **Correction**: $P = Q$ only in special cases; typically $P/Q$ is a nontrivial finite group

# Common Confusions
- **Confusion**: Thinking "weight" here refers to weights of specific representations
  **Clarification**: $P$ is the lattice of all possible integral weights; actual weights of a given representation form a subset of $P$

# Source Reference
Chapter 8: Root Systems, Section 8.5, pages 97--98. Equations (8.12), (8.13).

# Verification Notes
- Definition source: Direct from equation (8.12)
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified

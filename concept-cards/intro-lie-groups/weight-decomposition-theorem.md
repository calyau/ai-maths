---
# === CORE IDENTIFICATION ===
concept: Weight Decomposition Theorem
slug: weight-decomposition-theorem

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
pdf_page: 110
section: "9.1 Weight decomposition"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "weight decomposition"
  - "decomposition into weight spaces"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weight-of-representation
  - weight-space
  - cartan-subalgebra
extends: []
related:
  - weight-set
  - integral-weight
  - root-decomposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a representation decompose with respect to the Cartan subalgebra?"
  - "What must I know before studying representations of semisimple Lie algebras?"
---

# Quick Definition
The weight decomposition theorem states that every finite-dimensional representation of a semisimple Lie algebra decomposes as a direct sum of its weight spaces, and all weights are integral.

# Core Definition
**Theorem 9.2** (Kirillov, p. 110): Every finite-dimensional representation of $\mathfrak{g}$ admits a weight decomposition:

$$V = \bigoplus_{\lambda \in P(V)} V[\lambda].$$

Moreover, all weights of $V$ are integral: $P(V) \subset P$, where $P$ is the weight lattice.

# Prerequisites
- **Weight of a representation** -- the theorem asserts decomposition by weights
- **Weight space** -- the summands in the decomposition
- **Cartan subalgebra** -- the decomposition is with respect to $\mathfrak{h}$

# Key Properties
1. The decomposition is a direct sum (not just a sum)
2. All weights are integral (lie in the weight lattice $P$)
3. The number of weights is finite for finite-dimensional representations
4. The decomposition is compatible with the root decomposition: $\mathfrak{g}_\alpha \cdot V[\lambda] \subset V[\lambda + \alpha]$ (Lemma 9.3)
5. Submodules and quotients also admit weight decompositions (Lemma 9.11)

# Construction / Recognition
## To compute the weight decomposition
1. Choose a basis $h_1, \ldots, h_r$ for the Cartan subalgebra $\mathfrak{h}$
2. Simultaneously diagonalize all $h_i$ acting on $V$ (possible since they commute and each is diagonalizable)
3. Group basis vectors by their common eigenvalues to obtain weight spaces

# Context & Application
The weight decomposition is the fundamental structural result for representations of semisimple Lie algebras. It generalizes the eigenspace decomposition for $\mathfrak{sl}(2, \mathbb{C})$ representations and provides the foundation for the highest weight theory that classifies all irreducible representations.

The proof relies on two key ingredients: (1) each $h_\alpha$ is diagonalizable (from $\mathfrak{sl}(2, \mathbb{C})$ theory), and (2) commuting diagonalizable operators can be simultaneously diagonalized.

# Examples
**Example** (p. 110): For $\mathfrak{sl}(2, \mathbb{C})$, this reduces to the decomposition of a representation into eigenspaces of $h$, as studied in Section 5.1.

**Example** (p. 111): The adjoint representation $\mathfrak{g}$ decomposes as $\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in R} \mathfrak{g}_\alpha$, which is the root decomposition.

# Relationships
## Builds Upon
- **Weight space** -- the summands
- **Cartan subalgebra** -- provides the commuting operators

## Enables
- **Highest weight representation** -- the existence of a maximal weight relies on the decomposition
- **Root action on weights** -- Lemma 9.3 describes how root vectors shift weights

## Related
- **Root decomposition** -- the weight decomposition of the adjoint representation

# Common Errors
- **Error**: Attempting to decompose a representation without first fixing a Cartan subalgebra
  **Correction**: The weight decomposition depends on the choice of $\mathfrak{h}$; different choices give conjugate decompositions

# Common Confusions
- **Confusion**: Thinking the weight decomposition is the same as the decomposition into irreducible subrepresentations
  **Clarification**: Weight decomposition decomposes by eigenvalues of $\mathfrak{h}$; irreducible decomposition decomposes by $\mathfrak{g}$-submodules. A single weight space can contribute to multiple irreducible summands.

# Source Reference
Chapter 9, Section 9.1, Theorem 9.2, p. 110-111. Proof uses Lemma 7.19 and Section 5.1.

# Verification Notes
- Definition source: Direct from Theorem 9.2
- Confidence rationale: Central theorem with complete proof in source
- Uncertainties: None
- Cross-reference status: Verified

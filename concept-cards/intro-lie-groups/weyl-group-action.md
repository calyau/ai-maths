---
# === CORE IDENTIFICATION ===
concept: Weyl Group Action
slug: weyl-group-action

# === CLASSIFICATION ===
category: root-systems
subcategory: weyl-group
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 92
section: "8.2. Automorphisms and Weyl group"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weyl-group
  - abstract-root-system
extends:
  - weyl-group
related:
  - weyl-chamber
  - simple-reflections
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Weyl group act on weights and roots?"
  - "What are the key properties of the Weyl group action?"
---

# Quick Definition
The Weyl group acts on the ambient space $E$ by orthogonal transformations, permuting roots, Weyl chambers, and lattice elements. Its action on Weyl chambers is simply transitive, and every root is in the $W$-orbit of some simple root.

# Core Definition
The Weyl group $W$ acts on $E$ by orthogonal transformations (Lemma 8.7, p. 92). Key properties of this action:
- $w(R) = R$ for all $w \in W$ (roots are permuted)
- $W$ acts simply transitively on the set of Weyl chambers (Corollary 8.38, p. 102)
- $R = W(\Pi)$: every root is $w(\alpha_i)$ for some $w \in W$ and $\alpha_i \in \Pi$ (Theorem 8.30(2), p. 100)

# Prerequisites
- **weyl-group** -- the group whose action is studied
- **abstract-root-system** -- the space on which $W$ acts

# Key Properties
1. $W$ permutes $R$: $w(R) = R$ for every $w \in W$
2. $W$ acts transitively on Weyl chambers (Theorem 8.25, p. 99)
3. $W$ acts simply transitively on Weyl chambers (Corollary 8.38, p. 102)
4. $R = W(\Pi)$: every root is in the orbit of a simple root (Theorem 8.30(2))
5. Different polarizations give Weyl-conjugate sets of simple roots (Corollary 8.29)
6. $W$ preserves the root lattice $Q$ and weight lattice $P$

# Construction / Recognition
The action is computed by expressing $w$ as a product of simple reflections $w = s_{i_1}\cdots s_{i_l}$ and applying each reflection in sequence.

# Context & Application
The Weyl group action unifies the theory: it shows all polarizations are equivalent (Corollary 8.29), enables recovery of $R$ from $\Pi$ (Corollary 8.33), and in representation theory governs the symmetry of weight multiplicities.

# Examples
**Example 8.8** (p. 92): For $A_{n-1}$, the Weyl group $S_n$ acts on $E = \{\lambda \in \mathbb{R}^n \mid \sum\lambda_i = 0\}$ by permuting coordinates. Every root $e_i - e_j$ is obtained from the simple root $e_1 - e_2$ by a suitable permutation.

# Relationships
## Builds Upon
- **weyl-group**

## Enables
- **weyl-chamber** -- chambers are the orbits of $C_+$ under $W$
- **simple-reflections** -- generate $W$ and its action

## Related
- **positive-roots** -- a fundamental domain for the $W$-action on roots

## Contrasts With
(none)

# Common Errors
- **Error**: Assuming the $W$-action on roots is free (one-to-one on individual roots)
  **Correction**: The action on roots has stabilizers; the action is free only on Weyl chambers

# Common Confusions
- **Confusion**: Thinking different polarizations give genuinely different structure
  **Clarification**: They differ only by a Weyl group element (Corollary 8.29)

# Source Reference
Chapter 8: Root Systems, Sections 8.2, 8.6, 8.7. Lemma 8.7, Theorem 8.25, Corollary 8.29, Theorem 8.30, Corollary 8.38.

# Verification Notes
- Definition source: Synthesized from multiple results
- Confidence rationale: HIGH -- all cited results are explicit theorems
- Uncertainties: None
- Cross-reference status: Verified

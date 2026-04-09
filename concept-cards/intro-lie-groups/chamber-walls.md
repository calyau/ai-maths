---
# === CORE IDENTIFICATION ===
concept: Chamber Walls
slug: chamber-walls

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
pdf_page: 99
section: "8.6. Weyl chambers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "walls of a Weyl chamber"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weyl-chamber
  - root-hyperplane
  - simple-roots
extends: []
related:
  - positive-weyl-chamber
  - transitive-weyl-action-on-chambers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the walls of a Weyl chamber?"
  - "How many walls does a Weyl chamber have?"
---

# Quick Definition
The walls of a Weyl chamber $C$ are the codimension-one faces of its closure $\overline{C}$, each contained in a root hyperplane $L_\alpha$. Every chamber has exactly $r = \operatorname{rank}(R)$ walls; the walls of $C_+$ are the hyperplanes $L_{\alpha_i}$ for simple roots $\alpha_i$.

# Core Definition
The boundary $\partial C$ is a union of finitely many codimension-one faces $F_i$ (Lemma 8.23(2), p. 99). Each $F_i$ lies in a root hyperplane $L_\alpha$; the hyperplanes containing the faces are called walls of $C$.

**Corollary 8.28** (p. 100): Every Weyl chamber has exactly $r = \operatorname{rank}(R)$ walls. The walls of $C_+$ are $L_{\alpha_1},\ldots,L_{\alpha_r}$ (the hyperplanes for simple roots).

# Prerequisites
- **weyl-chamber** -- walls are a property of chambers
- **root-hyperplane** -- walls lie in root hyperplanes
- **simple-roots** -- walls of $C_+$ correspond to simple roots

# Key Properties
1. Each wall is a codimension-one convex subset of a root hyperplane
2. Every chamber has exactly $r$ walls (Corollary 8.28)
3. Walls of $C_+$ are $L_{\alpha_i}$, $\alpha_i \in \Pi$
4. Two chambers sharing a wall are called adjacent
5. Adjacent chambers separated by $L_\alpha$ are related by $s_\alpha$ (Lemma 8.27)

# Construction / Recognition
The walls of $C_+ = \{\lambda \mid (\lambda,\alpha_i) > 0\}$ are obtained by setting one inequality to equality: wall $i$ is $\{\lambda \in \overline{C_+} \mid (\lambda,\alpha_i) = 0\}$.

# Context & Application
Walls mediate the connection between adjacent Weyl chambers. The proof that $W$ acts transitively on chambers (Theorem 8.25) works by walking through adjacent chambers, crossing one wall at a time.

# Examples
**Example**: For $A_2$ (rank 2), each Weyl chamber has 2 walls. The positive chamber has walls $L_{\alpha_1}$ and $L_{\alpha_2}$.

# Relationships
## Builds Upon
- **weyl-chamber**, **root-hyperplane**

## Enables
- **transitive-weyl-action-on-chambers** -- proof uses wall-crossing

## Related
- **positive-weyl-chamber** -- its walls are the simple root hyperplanes

## Contrasts With
(none)

# Common Errors
(none)

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.6, pages 99--100. Lemma 8.23, Corollary 8.28.

# Verification Notes
- Definition source: Direct from Lemma 8.23 and Corollary 8.28
- Confidence rationale: HIGH -- explicit
- Uncertainties: None
- Cross-reference status: Verified

---
# === CORE IDENTIFICATION ===
concept: Weyl Chamber
slug: weyl-chamber

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
pdf_page: 98
section: "8.6. Weyl chambers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "chamber"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
  - root-hyperplane
extends: []
related:
  - positive-weyl-chamber
  - weyl-group
  - polarization
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Weyl chamber?"
  - "How many Weyl chambers are there?"
---

# Quick Definition
A Weyl chamber is a connected component of $E \setminus \bigcup_{\alpha \in R} L_\alpha$, the complement of all root hyperplanes. The Weyl group acts simply transitively on the set of Weyl chambers.

# Core Definition
A Weyl chamber is a connected component of the complement to the root hyperplanes (Definition 8.22, p. 98):

$$C = \text{connected component of } \left(E \setminus \bigcup_{\alpha \in R} L_\alpha\right)$$

Each Weyl chamber is specified by a system of inequalities $\pm(\alpha,\lambda) > 0$, one for each pair $\alpha, -\alpha$.

# Prerequisites
- **abstract-root-system** -- the root system whose hyperplanes define chambers
- **root-hyperplane** -- the hyperplanes $L_\alpha$ whose complement is decomposed

# Key Properties
1. Each Weyl chamber is an open convex cone (Lemma 8.23)
2. Its closure $\overline{C}$ is an unbounded convex cone
3. Each chamber has exactly $r = \operatorname{rank}(R)$ walls (Corollary 8.28, p. 100)
4. The number of Weyl chambers equals $|W|$ (Corollary 8.38)
5. $W$ acts simply transitively on chambers (Corollary 8.38, p. 102)
6. Two chambers are adjacent if they share a codimension-one face
7. Any two chambers can be connected by a sequence of adjacent chambers (Lemma 8.26)
8. Adjacent chambers separated by $L_\alpha$ are related by $s_\alpha$ (Lemma 8.27)

# Construction / Recognition
A Weyl chamber is determined by choosing a sign $\pm$ for each root hyperplane:
$$C = \{\lambda \in E \mid \epsilon_\alpha(\alpha,\lambda) > 0 \text{ for all } \alpha \in R_+\}$$
where $\epsilon_\alpha \in \{+1,-1\}$.

# Context & Application
Weyl chambers are in bijection with polarizations of $R$ (Lemma 8.24, p. 99). The transitive $W$-action on chambers (Theorem 8.25) implies different polarizations yield $W$-equivalent simple root systems. This is the geometric basis for the classification being independent of polarization.

# Examples
**Example** (p. 98): For $A_2$, there are 6 Weyl chambers (since $|W| = |S_3| = 6$), shown in Figure 8.4.

**Example 8.32** (p. 101): For $A_{n-1}$, the positive Weyl chamber is $\{\lambda_1 \geq \cdots \geq \lambda_n\}$ and chambers are indexed by permutations $\sigma \in S_n$.

# Relationships
## Builds Upon
- **root-hyperplane** -- chambers are defined by hyperplane complements

## Enables
- **positive-weyl-chamber** -- the distinguished chamber corresponding to $R_+$
- **weyl-length** -- counts hyperplanes separating $C_+$ from $w(C_+)$

## Related
- **weyl-group** -- acts simply transitively on chambers
- **polarization** -- in bijection with chambers

## Contrasts With
(none)

# Common Errors
- **Error**: Thinking Weyl chambers include their boundaries
  **Correction**: Weyl chambers are open sets; the boundary points lie on root hyperplanes

# Common Confusions
- **Confusion**: Thinking walls of a chamber can be any root hyperplane
  **Clarification**: Each chamber has exactly $r$ walls, corresponding to the simple roots of the associated polarization (Corollary 8.28)

# Source Reference
Chapter 8: Root Systems, Section 8.6, pages 98--100. Definition 8.22, Lemma 8.23, Lemma 8.24, Theorem 8.25, Corollary 8.28.

# Verification Notes
- Definition source: Direct from Definition 8.22
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified

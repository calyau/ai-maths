---
# === CORE IDENTIFICATION ===
concept: Adjacent Weyl Chambers
slug: adjacent-weyl-chambers

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weyl-chamber
  - chamber-walls
extends: []
related:
  - transitive-weyl-action-on-chambers
  - reflection-in-root-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When are two Weyl chambers adjacent?"
  - "How are adjacent chambers related?"
---

# Quick Definition
Two Weyl chambers are adjacent if they share a common codimension-one face (wall). Adjacent chambers separated by hyperplane $L_\alpha$ are related by the reflection $s_\alpha$: $C' = s_\alpha(C)$.

# Core Definition
Two Weyl chambers $C, C'$ are adjacent if they share a common codimension-one face $F$ (p. 99). If $L_\alpha$ is the hyperplane containing $F$, then $C$ and $C'$ are said to be separated by $L_\alpha$.

**Lemma 8.27** (p. 99): If $C, C'$ are adjacent chambers separated by $L_\alpha$, then $s_\alpha(C) = C'$.

**Lemma 8.26** (p. 99): Any two Weyl chambers can be connected by a sequence of adjacent chambers.

# Prerequisites
- **weyl-chamber** -- the objects being compared
- **chamber-walls** -- adjacency requires a shared wall

# Key Properties
1. Adjacent chambers are on opposite sides of a root hyperplane
2. The reflection across the separating hyperplane maps one to the other (Lemma 8.27)
3. Any two chambers are connected by a path of adjacent ones (Lemma 8.26)
4. The minimum number of adjacency steps from $C_+$ to $w(C_+)$ is $l(w)$

# Construction / Recognition
Two chambers $C, C'$ are adjacent if their closures share a codimension-one face lying in some $L_\alpha$.

# Context & Application
Adjacency is the key geometric structure enabling the proof of Theorem 8.25 (transitive $W$-action on chambers). Walking from one chamber to another through adjacent chambers produces a product of reflections representing the connecting Weyl group element.

# Examples
**Example**: For $A_2$, the positive chamber $C_+$ is adjacent to exactly 2 chambers (one for each wall $L_{\alpha_1}$, $L_{\alpha_2}$), reached by $s_1(C_+)$ and $s_2(C_+)$.

# Relationships
## Builds Upon
- **weyl-chamber**, **chamber-walls**

## Enables
- **transitive-weyl-action-on-chambers** -- proof uses adjacency chains

## Related
- **reflection-in-root-system** -- maps adjacent chambers to each other

## Contrasts With
(none)

# Common Errors
(none)

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.6, page 99. Lemmas 8.26, 8.27.

# Verification Notes
- Definition source: Direct from p. 99
- Confidence rationale: HIGH -- explicit definition and lemmas
- Uncertainties: None
- Cross-reference status: Verified

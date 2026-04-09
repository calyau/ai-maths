---
# === CORE IDENTIFICATION ===
concept: Regular Element
slug: regular-element

# === CLASSIFICATION ===
category: root-systems
subcategory: simple-positive-roots
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 94
section: "8.4. Positive roots and simple roots"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "generic element"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
  - root-hyperplane
extends: []
related:
  - polarization
  - weyl-chamber
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a regular element in the context of root systems?"
---

# Quick Definition
A regular element is a vector $t \in E$ satisfying $(\alpha,t) \neq 0$ for every root $\alpha \in R$, i.e., $t$ does not lie on any root hyperplane. Regular elements are precisely the elements in the interior of Weyl chambers.

# Core Definition
An element $t \in E$ is called regular if $(\alpha,t) \neq 0$ for every $\alpha \in R$ (p. 94). Equivalently, $t \in E \setminus \bigcup_{\alpha \in R} L_\alpha$, i.e., $t$ lies in some Weyl chamber.

# Prerequisites
- **abstract-root-system** -- regularity is defined with respect to roots
- **root-hyperplane** -- regular means not on any $L_\alpha$

# Key Properties
1. The set of regular elements is the complement of finitely many hyperplanes, hence open and dense
2. Each connected component of the regular set is a Weyl chamber
3. Choosing a regular element $t$ determines a polarization $R = R_+ \sqcup R_-$
4. Two regular elements in the same Weyl chamber give the same polarization

# Construction / Recognition
Choose any $t \in E$ and check $(\alpha,t) \neq 0$ for all $\alpha \in R$.

# Context & Application
Regular elements initiate the chain: regular element $\to$ polarization $\to$ positive roots $\to$ simple roots $\to$ Dynkin diagram. They are the "starting point" for extracting combinatorial data from a root system.

# Examples
**Example**: For $A_2$, an element $t = (a,b,c)$ with $a + b + c = 0$ is regular iff $a \neq b$, $b \neq c$, $a \neq c$.

# Relationships
## Builds Upon
- **root-hyperplane** -- regular means avoiding all hyperplanes

## Enables
- **polarization** -- determined by a regular element
- **weyl-chamber** -- regular elements are chamber interiors

## Related
(none)

## Contrasts With
(none)

# Common Errors
(none)

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.4, page 94.

# Verification Notes
- Definition source: Direct from p. 94
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified

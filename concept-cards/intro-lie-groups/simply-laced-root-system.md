---
# === CORE IDENTIFICATION ===
concept: Simply-Laced Root System
slug: simply-laced-root-system

# === CLASSIFICATION ===
category: root-systems
subcategory: dynkin-diagrams
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 106
section: "8.8. Dynkin diagrams and classification of root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ADE type"
  - "simply laced"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-root-systems
extends: []
related:
  - long-and-short-roots
  - dynkin-diagram
contrasts_with:
  - long-and-short-roots

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a simply-laced root system?"
  - "Which root systems are simply laced?"
---

# Quick Definition
A simply-laced root system is one where all roots have the same length (equivalently, the Dynkin diagram has only single edges). The simply-laced types are $A_n$, $D_n$, $E_6$, $E_7$, $E_8$.

# Core Definition
The ratio $m = \max(\alpha,\alpha)/\min(\alpha,\alpha)$ equals the maximal edge multiplicity in the Dynkin diagram (Corollary 8.51, p. 106). Root systems with $m = 1$ (only single edges) are called simply-laced diagrams. These are types $A$, $D$, $E$.

# Prerequisites
- **classification-of-root-systems** -- simply-laced is a property of the classified types

# Key Properties
1. All roots have the same length
2. Dynkin diagram has only single edges (no double or triple edges)
3. Cartan matrix is symmetric ($a_{ij} = a_{ji}$)
4. Simply-laced types: $A_n$, $D_n$, $E_6$, $E_7$, $E_8$
5. Non-simply-laced types: $B_n$, $C_n$, $F_4$ ($m = 2$) and $G_2$ ($m = 3$)

# Construction / Recognition
Check the Dynkin diagram: if all edges are single, the system is simply laced.

# Context & Application
Simply-laced root systems have additional symmetry (all roots are $W$-conjugate) and simpler structure. Many results in representation theory take a cleaner form for simply-laced types. The ADE classification also appears in singularity theory, McKay correspondence, and other areas.

# Examples
**Example** (p. 106): Types $A_n$, $D_n$, $E_6$, $E_7$, $E_8$ are simply laced. Types $B_n$, $C_n$, $F_4$ have $m = 2$, and $G_2$ has $m = 3$.

# Relationships
## Builds Upon
- **classification-of-root-systems**

## Enables
- Simplified formulas in representation theory

## Related
- **dynkin-diagram** -- simply laced means only single edges

## Contrasts With
- **long-and-short-roots** -- only exist in non-simply-laced types

# Common Errors
(none)

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.8, page 106. Corollary 8.51.

# Verification Notes
- Definition source: Direct from Corollary 8.51
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified

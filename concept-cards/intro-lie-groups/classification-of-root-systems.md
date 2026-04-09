---
# === CORE IDENTIFICATION ===
concept: Classification of Root Systems
slug: classification-of-root-systems

# === CLASSIFICATION ===
category: root-systems
subcategory: dynkin-diagrams
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 105
section: "8.8. Dynkin diagrams and classification of root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 8.49"
  - "Dynkin classification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - dynkin-diagram
  - reducible-root-system
extends: []
related:
  - classical-root-systems
  - exceptional-root-systems
  - classification-of-semisimple-lie-algebras
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are all possible Dynkin diagrams?"
  - "How are root systems classified?"
---

# Quick Definition
Every reduced irreducible root system has a Dynkin diagram isomorphic to one of: $A_n$ ($n \geq 1$), $B_n$ ($n \geq 2$), $C_n$ ($n \geq 2$), $D_n$ ($n \geq 4$), $E_6$, $E_7$, $E_8$, $F_4$, or $G_2$. Conversely, each of these diagrams is realized by a root system. This is the complete classification.

# Core Definition
**Theorem 8.49** (p. 105): Let $R$ be a reduced irreducible root system. Then its Dynkin diagram is isomorphic to one of:

- **Classical types**: $A_n$ ($n \geq 1$), $B_n$ ($n \geq 2$), $C_n$ ($n \geq 2$), $D_n$ ($n \geq 4$)
- **Exceptional types**: $E_6$, $E_7$, $E_8$, $F_4$, $G_2$

The subscript equals the rank (number of vertices). Conversely, each diagram is realized by some root system.

# Prerequisites
- **dynkin-diagram** -- the objects being classified
- **reducible-root-system** -- classification reduces to the irreducible case

# Key Properties
1. 4 infinite families: $A_n$, $B_n$, $C_n$, $D_n$ (classical types)
2. 5 exceptional types: $E_6$, $E_7$, $E_8$, $F_4$, $G_2$
3. The letters $A,\ldots,G$ are conventional (first 7 letters); no deeper meaning (p. 106)
4. Low-rank coincidences: $B_1 = C_1 = A_1$, $B_2 = C_2$, $D_2 = A_1 \times A_1$, $D_3 = A_3$ (Remark 8.50)
5. The same notation is used for the root system and its Dynkin diagram
6. Simply-laced types ($A$, $D$, $E$): all roots equal length, $m = 1$
7. Non-simply-laced: $B$, $C$, $F$ have $m = 2$; $G_2$ has $m = 3$ (Corollary 8.51)

# Construction / Recognition
The classification is proved by:
1. Showing the Dynkin diagram determines the root system (Theorem 8.48)
2. Determining which graphs can be Dynkin diagrams (constraints from integrality and positive-definiteness)
3. Explicitly constructing root systems for each allowed diagram (Appendix C)

# Context & Application
This is the culminating result of Chapter 8 and one of the most famous classification theorems in mathematics. Combined with the Serre relations (Section 8.9), it yields the classification of simple Lie algebras. The classical types correspond to matrix Lie algebras ($\mathfrak{sl}$, $\mathfrak{so}$, $\mathfrak{sp}$); the exceptional types are genuinely new.

# Examples
**Example** (p. 106): $A_n$ corresponds to $\mathfrak{sl}(n+1,\mathbb{C})$. Series $B_n$, $C_n$, $D_n$ correspond to $\mathfrak{so}$ and $\mathfrak{sp}$.

# Relationships
## Builds Upon
- **dynkin-diagram** -- the diagrams being classified
- **reducible-root-system** -- reduces to irreducible case

## Enables
- **classification-of-semisimple-lie-algebras** -- via the Serre relations bijection

## Related
- **classical-root-systems** -- the four infinite families
- **exceptional-root-systems** -- the five sporadic types

## Contrasts With
(none)

# Common Errors
- **Error**: Forgetting low-rank coincidences and listing redundant types
  **Correction**: $B_1 = C_1 = A_1$, $B_2 = C_2$, $D_2 = A_1 \times A_1$, $D_3 = A_3$ (Remark 8.50)

# Common Confusions
- **Confusion**: Thinking the classification includes non-reduced root systems
  **Clarification**: Theorem 8.49 classifies reduced irreducible root systems only

# Source Reference
Chapter 8: Root Systems, Section 8.8, pages 105--106. Theorem 8.49, Remark 8.50, Corollary 8.51.

# Verification Notes
- Definition source: Direct from Theorem 8.49
- Confidence rationale: HIGH -- the main classification theorem, stated explicitly
- Uncertainties: Proof is not given in the text (references [12], [11], [2])
- Cross-reference status: Verified

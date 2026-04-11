---
concept: Right Group Action
slug: right-group-action
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 131
section: "4.3 Groups Acting on Themselves by Conjugation"
extraction_confidence: high
aliases: []
prerequisites:
  - group-action
extends:
  - group-action
related:
  - conjugation-action
contrasts_with:
  - group-action
answers_questions:
  - "What is a right group action?"
  - "How do left and right actions differ?"
---

# Quick Definition
A right group action of G on A is a map A x G -> A, written a . g, satisfying (1) (a . g_1) . g_2 = a . (g_1 g_2), and (2) a . 1 = a. Given a left action, the map a . g = g^{-1} . a defines a corresponding right action with the same orbits.

# Core Definition
One can define a right group action of the group G on the nonempty set A as a map from A x G to A, denoted a . g, satisfying (1) (a . g_1) . g_2 = a . (g_1 g_2) and (2) a . 1 = a (Dummit & Foote, p. 131). For corresponding left and right actions, g acts on the left the same way g^{-1} acts on the right. The orbits are the same for corresponding actions. In much of group theory literature, conjugation is written as a right action: a^g = g^{-1}ag.

# Prerequisites
- **Group action** — Right actions are the dual notion to left actions

# Key Properties
1. Axiom: (a . g_1) . g_2 = a . (g_1 g_2) (note the order)
2. Given left action g . a, the map a . g = g^{-1} . a is a right action
3. Corresponding left and right actions have the same orbits
4. Right conjugation notation: a^g = g^{-1}ag satisfies laws of exponentiation

# Relationships
## Builds Upon
- **Group action** — Right actions are defined analogously
## Contrasts With
- **Group action** — Left: g_1 . (g_2 . a) = (g_1 g_2) . a; Right: (a . g_1) . g_2 = a . (g_1 g_2)

# Source Reference
Chapter 4, Section 4.3, pages 131-132.

# Verification Notes
- Definition source: Direct from p. 131
- Confidence: HIGH
- Uncertainties: None

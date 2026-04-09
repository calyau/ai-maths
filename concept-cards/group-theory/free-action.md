---
# === CORE IDENTIFICATION ===
concept: Free Action
slug: free-action

# === CLASSIFICATION ===
category: group-actions
subcategory: action-properties
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 58
section: "Stabilizers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - stabilizer
extends:
  - group-action
related:
  - faithful-action
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a free group action?"
---

# Quick Definition

An action is free if every stabilizer is trivial: $\operatorname{Stab}(x) = \{e\}$ for all $x \in X$.

# Core Definition

"The action is free if $\operatorname{Stab}(x) = \{e\}$ for all $x$" (Milne, p. 58).

# Prerequisites

- **Group action** — Freeness is a property of an action
- **Stabilizer** — Free means all stabilizers are trivial

# Key Properties

1. Free means no non-identity element fixes any point
2. Free implies faithful (but not conversely)
3. If the action is free and transitive, then $|X| = |G|$
4. Left multiplication of $G$ on itself is free and transitive

# Context & Application

Free actions arise in topology (covering spaces) and in the construction of quotient structures where no "collapsing" occurs at fixed points.

# Examples

**Example 1** (p. 56): $G$ acts freely on itself by left translation: if $gx = x$ then $g = 1$.

# Relationships

## Builds Upon
- **group-action**, **stabilizer**

## Related
- **faithful-action** — Free implies faithful

# Source Reference

Chapter 4: Groups Acting on Sets, "Stabilizers", page 58.

# Verification Notes

- Definition source: Direct from p. 58
- Confidence: HIGH — explicit definition
- Uncertainties: None

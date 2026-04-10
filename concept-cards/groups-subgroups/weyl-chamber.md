---
concept: Weyl Chamber
slug: weyl-chamber
category: root-systems
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 297
section: "The Weyl group"
extraction_confidence: high
aliases: []
prerequisites:
  - root-system
  - weyl-group
extends: []
related:
  - base-of-root-system
  - borel-subgroup
contrasts_with: []
answers_questions:
  - "What is a Weyl chamber?"
---

# Quick Definition

A Weyl chamber is a connected component of the complement V \ ∪_{α∈R} H_α, where H_α is the reflecting hyperplane of the root α. The Weyl group acts simply transitively on the set of Weyl chambers.

# Core Definition

Let (V, R) be a root system. For α ∈ R, let H_α denote the hyperplane of vectors fixed by s_α. A **Weyl chamber** is a connected component of V \ ∪_{α ∈ R} H_α (Milne, §1c, p. 297).

# Prerequisites

- **Root system** — The hyperplanes H_α are defined from the roots
- **Weyl group** — Acts simply transitively on the chambers

# Key Properties

1. W(R) acts simply transitively on the set of Weyl chambers (Proposition 1.8)
2. Each Weyl chamber determines a unique base S for R (Proposition 1.10)
3. A point t in a Weyl chamber satisfies ⟨t, α^∨⟩ ≠ 0 for all α ∈ R
4. Given a Weyl chamber containing t, the positive roots are R⁺ = {α ∈ R | (α,t) > 0}

# Context & Application

Weyl chambers provide a geometric way to understand bases, positive root systems, and Borel subgroups. Choosing a Weyl chamber is equivalent to choosing a base for R, and in the algebraic group setting, to choosing a Borel subgroup containing a given maximal torus.

# Examples

**Example 1** (p. 299): For the rank 2 root systems, the Weyl chambers are the sectors between adjacent reflecting lines. For A₂, there are 6 chambers (one for each element of W ≅ S₃).

# Relationships

## Builds Upon
- **Root system** — Chambers are defined by root hyperplanes

## Enables
- **Base of root system** — Each chamber determines a base
- **Borel subgroup** — Borel subgroups containing T correspond to chambers

# Source Reference

Chapter III, Section 1c, page 297. See also figures on pp. 299–300.

# Verification Notes

- Definition source: Direct from §1c, p. 297
- Confidence: HIGH — explicit definition
- Uncertainties: None

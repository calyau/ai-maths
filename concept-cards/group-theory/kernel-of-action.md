---
# === CORE IDENTIFICATION ===
concept: Kernel of an Action
slug: kernel-of-action

# === CLASSIFICATION ===
category: group-actions
subcategory: definitions
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
extends: []
related:
  - faithful-action
  - normal-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the kernel of a group action?"
---

# Quick Definition

The kernel of an action of $G$ on $X$ is $\ker(G \to \operatorname{Sym}(X)) = \bigcap_{x \in X} \operatorname{Stab}(x)$, the set of elements acting trivially on all of $X$.

# Core Definition

$\bigcap_{x \in X} \operatorname{Stab}(x) = \ker(G \to \operatorname{Sym}(X))$, which is a normal subgroup of $G$ (Milne, p. 58). The action is faithful if and only if this kernel is $\{1\}$.

# Prerequisites

- **Group action** — The kernel is defined for an action
- **Stabilizer** — The kernel is the intersection of all stabilizers

# Key Properties

1. The kernel is a normal subgroup of $G$
2. The kernel is trivial iff the action is faithful
3. For transitive actions with basepoint $x_0$: the kernel is the largest normal subgroup of $G$ contained in $\operatorname{Stab}(x_0)$ (Proposition 4.9)

# Context & Application

The kernel measures how much of $G$ is "invisible" in the action. Quotienting by the kernel gives a faithful action.

# Relationships

## Related
- **faithful-action** — Faithful iff kernel is trivial
- **normal-subgroup** — The kernel is always normal

# Source Reference

Chapter 4: Groups Acting on Sets, "Stabilizers", page 58.

# Verification Notes

- Definition source: Direct from p. 58
- Confidence: HIGH — explicit statement
- Uncertainties: None

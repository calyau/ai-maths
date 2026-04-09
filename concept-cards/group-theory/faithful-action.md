---
# === CORE IDENTIFICATION ===
concept: Faithful Action
slug: faithful-action

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
pdf_page: 56
section: "Definition and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - effective action

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends:
  - group-action
related:
  - stabilizer
contrasts_with:
  - transitive-action

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I verify that a group action is faithful?"
  - "What is the difference between a faithful and a transitive group action?"
---

# Quick Definition

A group action is faithful if the only element acting as the identity on all of $X$ is the identity element of $G$.

# Core Definition

"The action is said to be faithful (or effective) if the homomorphism $G \to \operatorname{Sym}(X)$ is injective, i.e., if $gx = x$ for all $x \in X \implies g = 1$" (Milne, p. 56).

# Prerequisites

- **Group action** — Faithfulness is a property of an action

# Key Properties

1. Equivalent to: the homomorphism $G \to \operatorname{Sym}(X)$ is injective
2. Equivalent to: $\bigcap_{x \in X} \operatorname{Stab}(x) = \{1\}$ (p. 58)
3. A faithful action embeds $G$ into $\operatorname{Sym}(X)$
4. Every subgroup of $\operatorname{Sym}(X)$ acts faithfully on $X$

# Construction / Recognition

## To verify faithfulness:
1. Show that if $gx = x$ for all $x \in X$, then $g = 1$
2. Equivalently, show $\ker(G \to \operatorname{Sym}(X)) = \{1\}$
3. Equivalently, show $\bigcap_{x \in X} \operatorname{Stab}(x) = \{1\}$

# Context & Application

Faithful actions realize $G$ concretely as a permutation group. Cayley's theorem shows every group has a faithful action (on itself by left multiplication).

# Examples

**Example 1** (p. 56): Any subgroup of $\operatorname{Sym}(X)$ acts faithfully on $X$.

**Example 2** (p. 56): $H$ acts faithfully on $G$ by left translation for any $H \leq G$.

**Example 3** (p. 56): $G$ acts faithfully on $G/H$ if $H \neq G$ and $G$ is simple.

# Relationships

## Builds Upon
- **group-action** — Faithfulness is a property of actions

## Contrasts With
- **transitive-action** — Faithfulness and transitivity are independent properties: an action can be one, both, or neither

# Common Confusions

- **Confusion**: Thinking faithful implies transitive or vice versa
  **Clarification**: These are independent properties. $G$ acting on itself by conjugation is neither faithful (centre acts trivially) nor transitive (unless $G = 1$)

# Source Reference

Chapter 4: Groups Acting on Sets, "Definition and examples", page 56.

# Verification Notes

- Definition source: Direct from p. 56
- Confidence: HIGH — explicit definition
- Uncertainties: None

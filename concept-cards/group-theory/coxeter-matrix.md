---
# === CORE IDENTIFICATION ===
concept: Coxeter Matrix
slug: coxeter-matrix

# === CLASSIFICATION ===
category: free-groups-presentations
subcategory: coxeter-groups
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Free Groups and Presentations; Coxeter Groups"
chapter_number: 2
pdf_page: 38
section: "Coxeter groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Coxeter function

# === TYPED RELATIONSHIPS ===
prerequisites:
  - coxeter-system
extends: []
related:
  - coxeter-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Coxeter matrix?"
  - "How does the Coxeter matrix determine a Coxeter group?"
---

# Quick Definition

A Coxeter matrix is a symmetric function $m: S \times S \to \mathbb{N} \cup \{\infty\}$ with $m(s,s) = 1$ and $m(s,t) \ge 2$ for $s \neq t$. It determines a Coxeter system and hence a Coxeter group.

# Core Definition

A Coxeter system is defined by a set $S$ and a mapping $m: S \times S \to \mathbb{N} \cup \{\infty\}$ satisfying: $m(s,s) = 1$ for all $s$; $m(s,t) \ge 2$ for $s \neq t$; $m(s,t) = m(t,s)$. (Milne, p. 38, Equation 14)

The group is then $G = \langle S \mid R \rangle$ where $R = \{(st)^{m(s,t)} \mid m(s,t) \neq \infty\}$.

# Prerequisites

- **Coxeter system** — the matrix defines a Coxeter system

# Key Properties

1. The matrix entries are integers $\ge 1$ (or $\infty$), with 1s on the diagonal
2. $m(s,t) = 2$ means $s$ and $t$ commute (since $(st)^2 = 1 \Rightarrow st = ts$)
3. $m(s,t) = \infty$ means no relation is imposed between $s$ and $t$
4. Often displayed as a Coxeter diagram (nodes for generators, edges labeled by $m(s,t)$)

# Context & Application

The Coxeter matrix (or equivalently, the Coxeter diagram) is the standard way to classify Coxeter groups. The classification of finite Coxeter groups yields the famous $A_n, B_n, D_n, E_6, E_7, E_8, F_4, H_3, H_4, I_2(m)$ types.

# Examples

**Example 1**: For $D_n$ (rank 2): $m(s,t) = n$, giving $\langle s, t \mid s^2, t^2, (st)^n \rangle$.

**Example 2**: For $S_n$ (type $A_{n-1}$): generators $s_1, \ldots, s_{n-1}$ with $m(s_i, s_{i+1}) = 3$ and $m(s_i, s_j) = 2$ for $|i-j| \ge 2$.

# Relationships

## Builds Upon
- **coxeter-system**

## Related
- **coxeter-group** — determined by the matrix

# Source Reference

Chapter 2, page 38, Equation 14.

# Verification Notes

- Definition source: Direct from p. 38
- Confidence: HIGH
- Uncertainties: None

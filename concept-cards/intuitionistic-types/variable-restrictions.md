---
# === CORE IDENTIFICATION ===
concept: Variable Restrictions
slug: variable-restrictions

# === CLASSIFICATION ===
category: formal-system
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Formalization of an Intuitionistic Theory of Types"
chapter_number: 2
pdf_page: 9
section: "2.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "binding restrictions"
  - "eigenvariable conditions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable
  - dependence
extends: []
related:
  - pi-introduction-rule
  - sigma-introduction-rule
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding dependent types?"
---

# Quick Definition

Variable restrictions are the conditions that prohibit binding a variable in a term or type if a free variable of that term or type has a type that depends on the variable being bound.

# Core Definition

Martin-Lof writes in Section 2.1: "There will be variable restrictions prohibiting us to bind a variable in a term or type if there is a free variable in the said term or type whose type depends on the variable in question. These variable restrictions contain as special cases those stated by Gentzen for his system of natural deduction for first order logic."

To avoid explicit mention of these restrictions, Martin-Lof adopts a notational convention: "a term which is denoted by b[x_1,...,x_n] contains no free variable distinct from x_{m+1},...,x_n whose type depends on x_m, m = 1,...,n."

# Prerequisites

- variable: The restrictions constrain which variables may be bound.
- dependence: The restrictions are formulated in terms of the dependence relation.

# Key Properties

1. One cannot bind a variable x if any free variable in the expression has a type that depends on x.
2. These restrictions generalize Gentzen's eigenvariable conditions for natural deduction.
3. The restrictions are automatically satisfied when the notational convention b[x_1,...,x_n] is used, because the convention tacitly excludes problematic free variables.
4. The restrictions ensure that binding operations produce well-formed types and terms.

# Construction / Recognition

## To Check a Binding Operation:
1. Suppose you wish to bind variable x in expression e.
2. List all free variables y of e that are distinct from x.
3. For each such y, determine whether the type of y depends on x.
4. If any such y has a type depending on x, the binding is prohibited.

## Example Check:
If y has type B[x] (depending on x), and y appears free in e, then one cannot bind x in e.

# Context & Application

Variable restrictions are essential for the well-formedness of terms involving lambda-abstraction, Pi-types, and Sigma-types. Without them, binding a variable could leave a "dangling dependency" -- a free variable whose type refers to a now-bound variable, making the expression ill-typed. Gentzen's original eigenvariable conditions for first order logic are a special case: they prevent universal generalization and existential instantiation over variables that appear in undischarged hypotheses.

# Examples

Suppose x is a variable of type A and y is a variable of type B[x]. The expression b[x, y] depends on both x and y. One cannot bind x in b[x, y] (via lambda, Pi, or Sigma) while y remains free, because the type B[x] of the free variable y depends on x.

However, if one first binds y (e.g., forming (lambda y)b[x, y]), then x may subsequently be bound in the resulting expression, since y is no longer free.

# Relationships

## Builds Upon
- variable: The restrictions concern the binding of variables.
- dependence: The restrictions are stated in terms of type-dependence on variables.

## Enables
- pi-introduction-rule: Lambda-abstraction must respect variable restrictions.
- sigma-introduction-rule: The Sigma type formation must respect variable restrictions.

## Related
- type-formation-rules: Type formation via Pi and Sigma involves binding and hence variable restrictions.

# Common Errors

- **Error**: Binding a variable x while a free variable y with type depending on x remains in the expression.
  **Correction**: Either bind y first or substitute a closed term for y before binding x.

# Common Confusions

- **Confusion**: Thinking variable restrictions only prevent binding variables that appear free in the expression.
  **Clarification**: The restriction is more subtle: it prohibits binding x even if x does not appear free, as long as some other free variable's *type* depends on x.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.1: variable restrictions and notational conventions.

# Verification Notes

Confidence: high. The restrictions are explicitly described in Section 2.1 and their relationship to Gentzen's conditions is stated by the author.

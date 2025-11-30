from typing import TypedDict
from langgraph.graph import StateGraph, END


# Load finance knowledge base from text file
def load_knowledge_base(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()


FINANCE_KNOWLEDGE = load_knowledge_base("finance_knowledge.txt")


# 1. Define the state that flows through the graph
class FinanceState(TypedDict):
    income: float
    expenses: float
    savings: float
    result_message: str
    savings_rate: float
    expense_ratio: float
    emergency_months: float


# 2. Node 1: Basic financial analysis (ratios)
def analysis_node(state: FinanceState) -> FinanceState:
    income = state["income"]
    expenses = state["expenses"]
    savings = state["savings"]

    if income <= 0:
        state["result_message"] = "Income must be greater than 0 to analyse finances."
        state["savings_rate"] = 0.0
        state["expense_ratio"] = 0.0
        state["emergency_months"] = 0.0
        return state

    savings_rate = savings / income
    expense_ratio = expenses / income
    emergency_months = savings / expenses if expenses > 0 else 0.0

    state["savings_rate"] = savings_rate
    state["expense_ratio"] = expense_ratio
    state["emergency_months"] = emergency_months

    return state


# 3. Node 2: Mistake detection, scoring, recommendations, and simple RAG explanations
def recommendation_node(state: FinanceState) -> FinanceState:
    income = state["income"]
    expenses = state["expenses"]
    savings = state["savings"]
    savings_rate = state["savings_rate"]
    expense_ratio = state["expense_ratio"]
    emergency_months = state["emergency_months"]

    # If analysis already set an error message
    if income <= 0:
        return state

    lines = [
        f"Monthly income: {income:.2f}",
        f"Monthly expenses: {expenses:.2f}",
        f"Monthly savings: {savings:.2f}",
        f"Savings rate: {savings_rate:.2%}",
        f"Expense-to-income ratio: {expense_ratio:.2%}",
        f"Emergency fund coverage: {emergency_months:.2f} months of expenses",
        "",
    ]

    mistakes = []

    # Savings rule
    if savings_rate < 0.10:
        mistakes.append("Very low savings rate (less than 10% of income).")
    elif savings_rate < 0.20:
        mistakes.append("Savings rate is below recommended 20% of income.")

    # Expense rule
    if expense_ratio > 0.80:
        mistakes.append("Expenses are more than 80% of income (very tight budget).")
    elif expense_ratio > 0.70:
        mistakes.append("Expenses are more than 70% of income (limited flexibility).")

    # Emergency fund rule
    if emergency_months < 1:
        mistakes.append("No emergency fund (less than 1 month of expenses saved).")
    elif emergency_months < 3:
        mistakes.append("Emergency fund is small (less than 3 months of expenses).")

    # Health score
    score = 100

    if savings_rate < 0.10:
        score -= 30
    elif savings_rate < 0.20:
        score -= 15

    if expense_ratio > 0.80:
        score -= 30
    elif expense_ratio > 0.70:
        score -= 15

    if emergency_months < 1:
        score -= 20
    elif emergency_months < 3:
        score -= 10

    if score < 0:
        score = 0

    lines.append(f"Financial health score: {score}/100")

    if mistakes:
        lines.append("")
        lines.append("Detected issues:")
        for m in mistakes:
            lines.append(f"- {m}")

        lines.append("")
        lines.append("Recommended actions to improve your finances:")

        # Expense management advice
        if expense_ratio > 0.70:
            target_expenses = 0.70 * income
            cut_needed = expenses - target_expenses
            if cut_needed > 0:
                lines.append(
                    f"- Try to reduce your monthly expenses by about {cut_needed:.2f} "
                    f"to bring them under 70% of your income."
                )

        # Savings advice
        if savings_rate < 0.20:
            target_savings = 0.20 * income
            extra_savings_needed = target_savings - savings
            if extra_savings_needed > 0:
                lines.append(
                    f"- Try to increase your monthly savings by about {extra_savings_needed:.2f} "
                    f"to reach a 20% savings rate."
                )

        # Emergency fund advice
        if emergency_months < 3 and expenses > 0:
            target_emergency = 3 * expenses
            extra_needed = target_emergency - savings
            if extra_needed > 0:
                lines.append(
                    f"- Build an emergency fund of at least 3 months of expenses. "
                    f"You need about {extra_needed:.2f} more saved."
                )

        # --- Simple RAG-style explanations from knowledge base (hard-coded from your rules) ---
        lines.append("")
        lines.append("Why these issues matter (from knowledge base):")

        if savings_rate < 0.20:
            lines.append(
                "- Savings Rule: Financial planners generally recommend saving at least "
                "20 percent of monthly income to build long-term wealth and financial security."
            )

        if expense_ratio > 0.70:
            lines.append(
                "- Expense Rule: If monthly expenses exceed 70 percent of income, the individual "
                "may face budgeting stress and limited flexibility for emergencies and investments."
            )

        if emergency_months < 3:
            lines.append(
                "- Emergency Fund Rule: A basic emergency fund should cover at least 3 to 6 months "
                "of essential living expenses to protect against job loss or medical emergencies."
            )
    else:
        lines.append("")
        lines.append("No major issues detected based on these simple rules. Good job!")

    state["result_message"] = "\n".join(lines)
    return state


# 4. Build a LangGraph with multiple nodes
graph_builder = StateGraph(FinanceState)

graph_builder.add_node("analysis", analysis_node)
graph_builder.add_node("recommendation", recommendation_node)

graph_builder.set_entry_point("analysis")
graph_builder.add_edge("analysis", "recommendation")
graph_builder.add_edge("recommendation", END)

graph = graph_builder.compile()


# Helper to run one analysis
def run_analysis(income: float, expenses: float, savings: float) -> str:
    initial_state: FinanceState = {
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "result_message": "",
        "savings_rate": 0.0,
        "expense_ratio": 0.0,
        "emergency_months": 0.0,
    }
    result = graph.invoke(initial_state)
    return result["result_message"]


# 5. Chatbot Loop + Mode Choice
if __name__ == "__main__":
    print("=== Personal Finance Mistake Detector Chatbot ===")

    while True:
        print("\nChoose a mode:")
        print("1. Full Financial Analysis")
        print("2. What-If Simulation Only")
        print("3. Exit")

        mode = input("Enter your choice (1/2/3): ").strip()

        if mode == "3":
            print("Goodbye! Stay financially healthy 😊")
            break

        income = float(input("\nEnter your monthly income: "))
        expenses = float(input("Enter your monthly expenses: "))
        savings = float(input("Enter your monthly savings: "))

        if mode == "1":
            print("\n--- Current Situation Analysis ---")
            print(run_analysis(income, expenses, savings))

            choice = input(
                "\nDo you want to run a what-if scenario? (y/n): "
            ).strip().lower()
            if choice == "y":
                new_expenses = float(input("What-if monthly expenses: "))
                new_savings = float(input("What-if monthly savings: "))
                print("\n--- What-If Scenario Result ---")
                print(run_analysis(income, new_expenses, new_savings))

        elif mode == "2":
            print("\n--- What-If Simulation ---")
            new_expenses = float(input("What-if monthly expenses: "))
            new_savings = float(input("What-if monthly savings: "))
            print("\n--- What-If Scenario Result ---")
            print(run_analysis(income, new_expenses, new_savings))

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

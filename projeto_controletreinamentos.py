from datetime import datetime, timedelta
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="controle_treinamentos"
)

cursor = conexao.cursor()


def treinamentos_vencidos():
    hoje = datetime.today().date()

    sql = """
    SELECT f.nome, t.nome, ft.data_vencimento
    FROM funcionario_treinamento ft
    JOIN funcionarios f ON ft.funcionario_id = f.id
    JOIN treinamentos t ON ft.treinamento_id = t.id
    WHERE ft.data_vencimento < %s
    """

    cursor.execute(sql, (hoje,))
    resultados = cursor.fetchall()

    print("\nTREINAMENTOS VENCIDOS")
    print("-" * 50)

    if not resultados:
        print("Nenhum treinamento vencido.")
        return

    for funcionario, treinamento, vencimento in resultados:
        print(
            f"Funcionário: {funcionario} | "
            f"Treinamento: {treinamento} | "
            f"Venceu em: {vencimento}"
        )


def treinamentos_vencendo(dias=30):
    hoje = datetime.today().date()
    limite = hoje + timedelta(days=dias)

    sql = """
    SELECT f.nome, t.nome, ft.data_vencimento
    FROM funcionario_treinamento ft
    JOIN funcionarios f ON ft.funcionario_id = f.id
    JOIN treinamentos t ON ft.treinamento_id = t.id
    WHERE ft.data_vencimento BETWEEN %s AND %s
    """

    cursor.execute(sql, (hoje, limite))
    resultados = cursor.fetchall()

    print("\nTREINAMENTOS VENCENDO NOS PRÓXIMOS 30 DIAS")
    print("-" * 50)

    if not resultados:
        print("Nenhum treinamento vencendo.")
        return

    for funcionario, treinamento, vencimento in resultados:
        print(
            f"Funcionário: {funcionario} | "
            f"Treinamento: {treinamento} | "
            f"Vencimento: {vencimento}"
        )


def treinamentos_em_dia():
    hoje = datetime.today().date()
    limite = hoje + timedelta(days=30)

    sql = """
    SELECT f.nome, t.nome, ft.data_vencimento
    FROM funcionario_treinamento ft
    JOIN funcionarios f ON ft.funcionario_id = f.id
    JOIN treinamentos t ON ft.treinamento_id = t.id
    WHERE ft.data_vencimento > %s
    """

    cursor.execute(sql, (limite,))
    resultados = cursor.fetchall()

    print("\nTREINAMENTOS REALIZADOS E EM DIA")
    print("-" * 50)

    if not resultados:
        print("Nenhum treinamento em dia.")
        return

    for funcionario, treinamento, vencimento in resultados:
        print(
            f"Funcionário: {funcionario} | "
            f"Treinamento: {treinamento} | "
            f"Válido até: {vencimento}"
        )


def treinamentos_nao_realizados():
    sql = """
    SELECT f.nome, t.nome
    FROM funcionarios f
    CROSS JOIN treinamentos t
    WHERE NOT EXISTS (
        SELECT 1
        FROM funcionario_treinamento ft
        WHERE ft.funcionario_id = f.id
        AND ft.treinamento_id = t.id
    )
    ORDER BY f.nome
    """

    cursor.execute(sql)
    resultados = cursor.fetchall()

    print("\nTREINAMENTOS NÃO REALIZADOS")
    print("-" * 50)

    if not resultados:
        print("Todos os treinamentos foram realizados.")
        return

    for funcionario, treinamento in resultados:
        print(
            f"Funcionário: {funcionario} | "
            f"Treinamento: {treinamento}"
        )


def painel():
    print("\n" + "=" * 60)
    print("PAINEL DE CONTROLE DE TREINAMENTOS")
    print("=" * 60)

    treinamentos_vencidos()
    treinamentos_vencendo()
    treinamentos_em_dia()
    treinamentos_nao_realizados()


if __name__ == "__main__":
    try:
        painel()
    finally:
        cursor.close()
        conexao.close()
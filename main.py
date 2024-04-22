from Menu import Menu


def main():
    try:
        print("Iniciando programa...")
        m = Menu("Trenes S.A")
        m.mainloop()
    except Exception as e:
        print(f"Ha ocurrido la excepcion: {e}")


if __name__ == "__main__":
    main()

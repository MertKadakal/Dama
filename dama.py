import os
import time
os.system("cls")
print("Dama oyununa hoşgeldiniz\n\nOyun birkaç saniye içinde başlayacak...")
time.sleep(1)
os.system("cls")

table = [["·", "■", "·", "■", "·", "■", "·", "■"],
         ["■", "·", "■", "·", "■", "·", "■", "·"],
         ["·", "■", "·", "■", "·", "■", "·", "■"],
         ["·", "·", "·", "·", "·", "·", "·", "·"],
         ["·", "·", "·", "·", "·", "·", "·", "·"],
         ["□", "·", "□", "·", "□", "·", "□", "·"],
         ["·", "□", "·", "□", "·", "□", "·", "□"],
         ["□", "·", "□", "·", "□", "·", "□", "·"]]

"""table = [["·", "■", "·", "■", "○", "■", "·", "■"],
         ["■", "·", "■", "■", "·", "·", "■", "·"],
         ["·", "·", "·", "■", "·", "□", "·", "■"],
         ["·", "□", "·", "·", "·", "·", "■", "·"],
         ["·", "·", "·", "□", "·", "□", "·", "·"],
         ["□", "·", "·", "·", "·", "·", "·", "·"],
         ["·", "□", "·", "□", "·", "·", "□", "·"],
         ["·", "·", "·", "·", "·", "●", "·", "·"]]"""

symbls_of_ways = ["↖","↗","↙","↘"]
turn = "■"
white_got, black_got = 0, 0
one_got_piece = 0

def return_other_player(current_player):
    if current_player == "□":
        return "■"
    if current_player == "■":
        return "□"

def control_if_playable(x, y):
    possible_ways = []
    if turn == "□":
        # bir üst-solu kontrol et
        if y - 1 >= 0 and x - 1 >= 0 and table[x - 1][y - 1] == "·":
            possible_ways.append("10")
        # bir üst-sağı kontrol et
        if y + 1 <= 7 and x - 1 >= 0 and table[x - 1][y + 1] == "·":
            possible_ways.append("11")
    else:
        # bir alt-solu kontrol et
        if y - 1 >= 0 and x + 1 <= 7 and table[x + 1][y - 1] == "·":
            possible_ways.append("12")
        # bir alt-sağı kontrol et
        if y + 1 <= 7 and x + 1 <= 7 and table[x + 1][y + 1] == "·":
            possible_ways.append("13")
    return possible_ways

def control_if_double_move_available(x, y):
    possible_ways = []
    if y - 2 >= 0 and x - 2 >= 0:
        if table[x - 2][y - 2] == "·" and table[x - 1][y - 1] == return_other_player(turn):
            possible_ways.append("20")
    if y + 2 <= 7 and x - 2 >= 0:
        if table[x - 2][y + 2] == "·" and table[x - 1][y + 1] == return_other_player(turn):
            possible_ways.append("21")
    if y - 2 >= 0 and x + 2 <= 7:
        if table[x + 2][y - 2] == "·" and table[x + 1][y - 1] == return_other_player(turn):
            possible_ways.append("22")
    if y + 2 <= 7 and x + 2 <= 7:
        if table[x + 2][y + 2] == "·" and table[x + 1][y + 1] == return_other_player(turn):
            possible_ways.append("23")
    return possible_ways

def control_if_king_move_available():
    psbltys_of_ways = [[0,0,""],[0,0,""],[0,0,""],[0,0,""]]

    # sol-üst doğrultuyu kontrol et
    a = []
    b = 99
    i = 0
    while row2-1-i >= 0 and col2-1-i >= 0:
        a.append(table[row2-1-i][col2-1-i])
        i += 1
    for i in range(len(a)-1):
        if a[i] == a[i+1] == return_other_player(turn) or a[i] == turn:
            break
        elif a[i] == "·":
            b = i
        elif a[i] == return_other_player(turn) and a[i+1] == "·":
            b = i+1
    if b == len(a)-2:
        if a[b+1] == '·':
            b += 1
    if b != 99:
        psbltys_of_ways[0][0], psbltys_of_ways[0][1] = 1, b
        psbltys_of_ways[0][2] = a

    # sağ-üst doğrultuyu kontrol et
    a = []
    b = 99
    i = 0
    while row2-1-i >= 0 and col2+1+i < 8:
        a.append(table[row2-1-i][col2+1+i])
        i += 1
    for i in range(len(a) - 1):
        if a[i] == a[i + 1] == return_other_player(turn) or a[i] == turn:
            break
        elif a[i] == "·":
            b = i
        elif a[i] == return_other_player(turn) and a[i + 1] == "·":
            b = i + 1
    if b == len(a) - 2:
        if a[b + 1] == '·':
            b += 1
    if b != 99:
        psbltys_of_ways[1][0], psbltys_of_ways[1][1] = 1, b
        psbltys_of_ways[1][2] = a

    # sol-alt doğrultuyu kontrol et
    a = []
    b = 99
    i = 0
    while row2+1+i < 8 and col2-1-i >= 0:
        a.append(table[row2+1+i][col2-1-i])
        i += 1
    for i in range(len(a) - 1):
        if a[i] == a[i + 1] == return_other_player(turn) or a[i] == turn:
            break
        elif a[i] == "·":
            b = i
        elif a[i] == return_other_player(turn) and a[i + 1] == "·":
            b = i + 1
    if b == len(a) - 2:
        if a[b + 1] == '·':
            b += 1
    if b != 99:
        psbltys_of_ways[2][0], psbltys_of_ways[2][1] = 1, b
        psbltys_of_ways[2][2] = a

    # sağ-alt doğrultuyu kontrol et
    a = []
    b = 99
    i = 0
    while row2+1+i < 8 and col2+1+i < 8:
        a.append(table[row2+1+i][col2+1+i])
        i += 1
    for i in range(len(a) - 1):
        if a[i] == a[i + 1] == return_other_player(turn) or a[i] == turn:
            break
        elif a[i] == "·":
            b = i
        elif a[i] == return_other_player(turn) and a[i + 1] == "·":
            b = i + 1
    if b == len(a) - 2:
        if a[b + 1] == '·':
            b += 1
    if b != 99:
        psbltys_of_ways[3][0], psbltys_of_ways[3][1] = 1, b
        psbltys_of_ways[3][2] = a

    return psbltys_of_ways

def control_if_king_move_available_again(list): # bir king taşı hamle yapıp taş aldıktan sonra tekrar taş alarak hamle yapıp yapamayacağını kontrol eden fonksiyon
    if list != "":
        for i in range(len(list) - 1):
            if list[i] == return_other_player(turn) and list[i + 1] == "·":
                return True
        return False
    else:
        return False

def print_table_with_arrows(x, y):
    os.system("cls")
    print(y *3 * " " + "↓")
    for i in range(8):
        if i == x:
            print(*table[i], sep="  ", end="")
            print(" ←")
        else:
            print(*table[i], sep="  ")
def print_table_without_arrows():
    os.system("cls")
    print()
    for i in range(8):
        print(*table[i], sep="  ")
def move(ir, ic, dir, jump):
    global row2, col2, one_got_piece, white_got, black_got
    sağ_üst_rc = [ir-1, ic+1]
    sol_üst_rc = [ir-1, ic-1]
    sağ_alt_rc = [ir+1, ic+1]
    sol_alt_rc = [ir+1, ic-1]
    a = 0

    table[row2][col2] = "·"
    if jump == 1:
        if dir == 0:
            table[sol_üst_rc[0]][sol_üst_rc[1]] = turn
            row2 -= 1
            col2 -= 1
        if dir == 1:
            table[sağ_üst_rc[0]][sağ_üst_rc[1]] = turn
            row2 -= 1
            col2 += 1
        if dir == 2:
            table[sol_alt_rc[0]][sol_alt_rc[1]] = turn
            row2 += 1
            col2 -= 1
        if dir == 3:
            table[sağ_alt_rc[0]][sağ_alt_rc[1]] = turn
            row2 += 1
            col2 += 1
    else:
        if dir == 0:
            table[sol_üst_rc[0]][sol_üst_rc[1]] = "·"
            table[sol_üst_rc[0]-1][sol_üst_rc[1]-1] = turn
            row2 -= 2
            col2 -= 2
        if dir == 1:
            table[sağ_üst_rc[0]][sağ_üst_rc[1]] = "·"
            table[sağ_üst_rc[0]-1][sağ_üst_rc[1]+1] = turn
            row2 -= 2
            col2 += 2
        if dir == 2:
            table[sol_alt_rc[0]][sol_alt_rc[1]] = "·"
            table[sol_alt_rc[0]+1][sol_alt_rc[1]-1] = turn
            row2 += 2
            col2 -= 2
        if dir == 3:
            table[sağ_alt_rc[0]][sağ_alt_rc[1]] = "·"
            table[sağ_alt_rc[0]+1][sağ_alt_rc[1]+1] = turn
            row2 += 2
            col2 += 2
        a += 1
        if turn == "□":
            black_got += a
        else:
            white_got += a
        one_got_piece = turn

    if row2 == 0 or row2 == 7:
        if turn == "□":
            print("\n! Siyah, bir dama taşı elde etti")
            table[row2][col2] = "○"
        else:
            print("\n! Beyaz, bir dama taşı elde etti")
            table[row2][col2] = "●"

def change_the_turn():
    global turn
    if turn == "■":
        turn = "□"
    else:
        turn = "■"

print_table_without_arrows()
print("\nBeyaz başlar")

did_king_got_piece = 0
jumped_or_not = 0
row2, col2 = 4, 0

while True: # bu whiledan oyun bittikten sonra çıkılacak
    if jumped_or_not == 0: # eğer önceki hamlede rakip taş alınmadıysa bu ife girer    #and not control_if_double_move_available(row2, col2)"""#

        if (row2 == 0 or row2 == 7) and one_got_piece != 0:
            if row2 == 0:
                print("\n! Siyah, bir dama taşı elde etti")
                table[row2][col2] = "○"
            else:
                print("\n! Beyaz, bir dama taşı elde etti")
                table[row2][col2] = "●"

        if one_got_piece != 0:
            if one_got_piece == "□":
                print("\n! Siyah, beyaz taş(lar) aldı")
            else:
                print("\n! Beyaz, siyah taş(lar) aldı")
            print(f"\n! Toplamda: Beyaz'ın aldığı taşlar {white_got} - Siyah'ın aldığı taşlar {black_got}")
            one_got_piece = 0

        if turn == "■":
            print("\nSıra Beyaz'da")
        else:
            print("\nSıra Siyah'ta")

        if did_king_got_piece == 1:
            did_king_got_piece = 0
        else:
            row, col = input("─────────────────────────────────────────────────\n"
                             "Oynatmak istediğiniz taşın konumunu girin: ").split(" ")
            row2, col2 = int(row)-1, int(col)-1

        if int(row) > 8 or int(col) > 8:
            print("\n! Lütfen doğru bir konum girin")
        elif table[row2][col2] == "·":
            print("\n! Lütfen bir taşın olduğu konum girin") #"■""□""●""○"
        elif (table[row2][col2] == "●" or table[row2][col2] == "■") and turn == "□":
            print("\n! Lütfen siyah bir taş seçin")
        elif (table[row2][col2] == "○" or table[row2][col2] == "□") and turn == "■":
            print("\n! Lütfen beyaz bir taş seçin")
        elif not bool(control_if_playable(row2, col2)) and not bool(control_if_double_move_available(row2, col2)) and table[row2][col2] != "●" and table[row2][col2] != "○":
            print("\n! Bu taş hareket edemez")

        else: #tüm şartlardan olumlu geçtikten sonra taş hareket ettirilir
            os.system("cls")
            print_table_with_arrows(row2, col2)
            while True: # bu whiledan taş hareket ettirildikten sonra çıkılacak

                if table[row2][col2] == "●" or table[row2][col2] == "○": # hareket ettirilecek taş kingse bu ife girer
                    possible_ways = control_if_king_move_available()
                    a = []
                    for i in range(len(possible_ways)):
                        if possible_ways[i][0] != 0:
                            a.append(i)

                    b=""
                    if len(a) > 0:
                        for i in range(len(a)):
                            b += f"{i}: {symbls_of_ways[a[i]]} "

                    c = int(input(f"\nLütfen hangi yöne hareket ettirmek istediğiniz seçin {b}\n→"))
                    if possible_ways[a[c]][1] != 0:
                        while True:
                            b = input(f"\nLütfen hangi konuma hareket ettirmek istediğinizi girin: ").split(" ")
                            target_row, target_col = int(b[0])-1, int(b[1])-1
                            if abs(target_row-row2) <= possible_ways[a[c]][1] + 1 and abs(target_col-col2) <= possible_ways[a[c]][1] + 1 and abs(target_row-row2) == abs(target_col-col2) and table[target_row][target_col] == "·":
                                if (a[c] == 0 and target_row < row2 and target_col < col2) or (a[c] == 1 and target_row < row2 and target_col > col2) or (a[c] == 2 and target_row > row2 and target_col < col2) or (a[c] == 3 and target_row > row2 and target_col > col2):
                                    break
                                else:
                                    print("\n! Lütfen dama taşının gidebileceği bir konum girin")
                            else:
                                print("\n! Lütfen dama taşının gidebileceği bir konum girin")
                    else:
                        if a[c] == 0:
                            target_row, target_col = row2 - 1, col2 - 1
                        if a[c] == 1:
                            target_row, target_col = row2 - 1, col2 + 1
                        if a[c] == 2:
                            target_row, target_col = row2 + 1, col2 - 1
                        if a[c] == 3:
                            target_row, target_col = row2 + 1, col2 + 1

                    table[row2][col2] = "·"
                    if turn == "■":
                        table[target_row][target_col] = "●"
                    else:
                        table[target_row][target_col] = "○"

                    b = 0
                    if a[c] == 0:
                        while row2 > target_row and col2 > target_col:
                            row2 -= 1
                            col2 -= 1
                            if table[row2][col2] == return_other_player(turn):
                                table[row2][col2] = "·"
                                if turn == "■":
                                    white_got += 1
                                else:
                                    black_got += 1
                                one_got_piece = turn
                                b = 1

                    if a[c] == 1:
                        while row2 > target_row and col2 < target_col:
                            row2 -= 1
                            col2 += 1
                            if table[row2][col2] == return_other_player(turn):
                                table[row2][col2] = "·"
                                if turn == "■":
                                    white_got += 1
                                else:
                                    black_got += 1
                                one_got_piece = turn
                                b = 1

                    if a[c] == 2:
                        while row2 < target_row and col2 > target_col:
                            row2 += 1
                            col2 -= 1
                            if table[row2][col2] == return_other_player(turn):
                                table[row2][col2] = "·"
                                if turn == "■":
                                    white_got += 1
                                else:
                                    black_got += 1
                                one_got_piece = turn
                                b = 1

                    if a[c] == 3:
                        while row2 < target_row and col2 < target_col:
                            row2 += 1
                            col2 += 1
                            if table[row2][col2] == return_other_player(turn):
                                table[row2][col2] = "·"
                                if turn == "■":
                                    white_got += 1
                                else:
                                    black_got += 1
                                one_got_piece = turn
                                b = 1

                    if b == 1:
                        row2, col2 = target_row, target_col
                        a = control_if_king_move_available()
                        if control_if_king_move_available_again(a[0][2][:a[0][1]+1]) or control_if_king_move_available_again(a[1][2][:a[1][1]+1]) or control_if_king_move_available_again(a[2][2][:a[2][1]+1]) or control_if_king_move_available_again(a[3][2][:a[3][1]+1]):
                            row2, col2 = target_row, target_col
                            did_king_got_piece = 1
                        else:
                            row2 = 99
                            change_the_turn()
                    else:
                        row2 = 99
                        change_the_turn()

                    print_table_without_arrows()
                    break

                else: # hareket ettirilecek taş normal taşsa bu ife girer
                    possible_ways = sorted(control_if_playable(row2, col2) + control_if_double_move_available(row2, col2))
                    if len(possible_ways) != 1:
                        b = ""
                        for i in range(len(possible_ways)):
                            b += f"{i}: {symbls_of_ways[int(possible_ways[i][1])]} "

                        while True:
                            c = int(input(f"\nLütfen hangi yöne hareket ettirmek istediğiniz seçin {b}\n→"))
                            if  c < len(possible_ways):
                                a = possible_ways[c]
                                break
                            else:
                                print("\n! Lütfen doğru bir seçenek girin")
                        jump, slctd = int(a[0]), int(a[1])
                    else:
                        slctd = int(possible_ways[0][1])
                        jump = int(possible_ways[0][0])

                    move(row2, col2, slctd, jump)

                    if jump == 2 and control_if_double_move_available(row2, col2):
                        jumped_or_not = 1
                    else:
                        jumped_or_not = 0
                        change_the_turn()

                    print_table_without_arrows()
                    break
    else: # eğer önceki hamlede rakip taş alındıysa bu ife girer
        os.system("cls")
        print_table_with_arrows(row2, col2)
        while True:
            possible_ways = control_if_double_move_available(row2, col2)
            if len(possible_ways) != 1:
                b = ""
                for i in range(len(possible_ways)):
                    b += f"{i}: {symbls_of_ways[int(possible_ways[i][1])]} "

                while True:
                    c = int(input(f"\nLütfen hangi yöne hareket ettirmek istediğiniz seçin {b}\n→"))
                    if c < len(possible_ways):
                        a = possible_ways[c]
                        break
                    else:
                        print("\n! Lütfen doğru bir seçenek girin")
                jump, slctd = int(a[0]), int(a[1])
            else:
                slctd = int(possible_ways[0][1])
                jump = int(possible_ways[0][0])

            move(row2, col2, slctd, jump)

            if jump == 2 and control_if_double_move_available(row2, col2):
                jumped_or_not = 1
            else:
                jumped_or_not = 0
                change_the_turn()

            print_table_without_arrows()
            break

    if white_got == 12 or black_got == 12:
        os.system("cls")
        if white_got == 12:
            print("\n\n\n\n!!! BEYAZ OYUNU KAZANDI !!!\n\n\n\n")
        else:
            print("\n\n\n\n!!! SİYAH OYUNU KAZANDI !!!\n\n\n\n")
        break

    if white_got == black_got == 11:
        os.system("cls")
        print("\n\n\n\n!!! BERABERE !!!\n\n\n\n")
        break
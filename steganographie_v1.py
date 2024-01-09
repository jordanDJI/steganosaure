import cv2

def lsb1_stegano(image_path, message):
    image_array=cv2.imread(image_path)
    #rendre l'image paire
    image_array=image_array - image_array%2
    #convertir le message en binaire
    binary_message="".join(format(ord(carac), '08b') for carac in message)

    if len(binary_message)>image_array.size:
        raise Exception("La taille du message est superieur aux nombre de pixels de l'image")
    
    #on ecrit dans l'image
    nb_row,nb_cols, nb_canals = image_array.shape
    index_binary_messae=0
    for index_row in range(nb_row):
        for index_cols in range(nb_cols):
            for index_canals in range(nb_canals):
                if index_binary_messae < len(binary_message):
                    image_array[index_row, index_cols, index_canals] += int(binary_message[index_row, index_cols,index_canals])
                    index_binary_messae += 1
                else:
                    break

    cv2.imwrite("../stegano_img.png", image_array)

def lsb1_extract_message(stegano_img_path):
    stegano_img_array= cv2.imread(stegano_img_path)
    binary_array_message= stegano_img_array % 2

    nb_row,nb_cols,nb_canals=binary_array_message.shape

    binary_message_list= []

    for index_row in range(nb_row):
        for index_cols in range(nb_cols):
            for index_canals in range(nb_canals):

                binary_message_list.append(str(binary_array_message[index_row, index_cols, index_canals]))

    #on elimine les caracteres vides
    for index_binary_char in range(0,index_row*index_cols*index_canals,8):
        if binary_message_list[index_binary_char:index_binary_char+8]==["0"]*8:
            binary_message_list=binary_message_list[ : index_binary_char] #slicing
            break
    binary_message = "".join(binary_message_list)
    message = "".join([chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8)])
    print(message)

if  __name__ == "__main__":
    lsb1_stegano("../image_entree.png","coucou les loulou")
    lsb1_extract_message()



    # comprehention de list

    
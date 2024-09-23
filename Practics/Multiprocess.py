import multiprocessing as mp
from PIL import Image

data = []
queue = mp.Queue()


def resize_image(image_paths, queue):
    print(image_paths)
    for image_path in image_paths:
        image1 = Image.open(image_path)
        image1 = image1.resize((200, 200))
        queue.put((image_path, image1))



def chage_color(queue):
    while True:
        image_path, image2 = queue.get()
        image1 = image2.convert('L')
        image1.save(image_path)
        print(image_path)
        if queue.empty():
            exit()








if __name__ == '__main__':

    for i in range(10,20):
        data.append(f'D:/PycharmProjects/images/img ({i}).jpg')

    resize_process = mp.Process(target=resize_image, args=(data, queue))
    change_process = mp.Process(target=chage_color, args=(queue,))

    resize_process.start()
    change_process.start()

    # resize_process.join()
    # change_process.join()
    print('Change stopped')

    print('Resize stopped')
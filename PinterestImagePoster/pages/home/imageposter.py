import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pynput.keyboard import Key, Controller
import time

class PostImage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.keyboard = Controller()


    # Locators
    _profile = "//a[@href='/ben_g98/']"
    _upload_button = "//button[@aria-label='Profile actions overflow']"
    _create_pin_button = "//div[@title='Create Pin']"
    _upload_image_button = "//*[@id='media-upload-input']//parent::div"
    _upload_image_key = "media-upload-input"
    _image_title = "//textarea[@placeholder='Add your title']"
    _image_desc = "//textarea[@placeholder='Tell everyone what your Pin is about']"
    _board_menu = "//button[@data-test-id='board-dropdown-select-button']"
    _submit_button = "//button[@data-test-id='board-dropdown-save-button']"
    image_locators = ["C:\\Photos\\MyDog", "C:\\Photos\\YourDog", "C:\\Photos\\HerDog", "C:\\Photos\\HappyDog", "C:\\Photos\\SleepyDog", "C:\\Photos\\BabyDog"]

    def clickProfile(self):
        self.elementClick(self._profile, locatorType="xpath")

    def clickUploadButton(self):
        self.elementClick(self._upload_button, locatorType="xpath")

    def clickCreateAPin(self):
        self.elementClick(self._create_pin_button, locatorType="xpath")

    def addATitle(self, title="Check Out My New Image"):
        self.sendKeys(title, self._image_title, locatorType="xpath")

    def addADescription(self, description="This is my new image, do you like it?"):
        self.sendKeys(description, self._image_desc, locatorType="xpath")

    def clickUploadAnImage(self):
        self.elementClick(self._upload_image_button, locatorType="xpath")
        time.sleep(1)

    def typeInImage(self):
        numOfImages = len(self.image_locators)
        for image in range(0, numOfImages):
            self.keyboard.type(self.image_locators[image])
            time.sleep(1)
            self.keyboard.press(Key.enter)

    def accessBoards(self, boardName="Dogs"):
        _board_selection = "//div[@title='" + str(boardName) + "']"

        self.elementClick(self._board_menu, locatorType="xpath")
        try:
            self.elementClick(_board_selection, locatorType="xpath")
        except:
            print("Sorry, this board name was not found")

    def submitImage(self):
        self.elementClick(self._submit_button, locatorType="xpath")

    def ImageAutomation(self):
        self.clickProfile()
        time.sleep(2)
        self.clickUploadButton()
        time.sleep(2)
        self.clickCreateAPin()
        time.sleep(3)
        self.clickUploadAnImage()
        time.sleep(2)
        self.typeInImage()
        time.sleep(2)
        self.addATitle()
        time.sleep(2)
        self.addADescription()
        time.sleep(2)
        self.accessBoards()
        time.sleep(2)
        self.submitImage()
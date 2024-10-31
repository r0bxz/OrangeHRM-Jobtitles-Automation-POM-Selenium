from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.job_titles_page import JobTitlesPage
from data.test_data import TestData

def main():
    # Initialize the WebDriver
    service = Service(executable_path=TestData.DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(30)

    try:
        # Test Case 1: Login with valid credintials 
        driver.get(TestData.URL)
        login_page = LoginPage(driver)
        login_page.enter_username(TestData.USERNAME)
        login_page.enter_password(TestData.PASSWORD)
        login_page.click_login()

        # Test Case 2: Add Job Title
        job_titles_page = JobTitlesPage(driver)
        job_titles_page.add_job_title(TestData.job_title, TestData.description, TestData.FILE_PATH, TestData.note)
        job_titles_page.verify_job_title_added(TestData.job_title)
        print("Assertion passed. New job title was added to the list")
        
        # Test Case 3: Edit Job Title
        job_titles_page.edit_job_title(TestData.job_title, TestData.edited_job_title)
        job_titles_page.verify_job_title_added(TestData.edited_job_title)
        print("Assertion passed. Job title was updated to 'Editied Job Title'")
        

        # Test Case 4: Delete Job Title
        job_titles_page.delete_job_title(TestData.edited_job_title)
        job_titles_page.verify_job_title_deleted(TestData.edited_job_title)
        print("Assertion passed. Edited Job title was removed from the list.")
        

    except AssertionError as e:
        print(e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

# Main page

# "Guest log in" button on navigation panel
# 1) button.header-link.-guest
# 2) //button[text()='Guest log in' and contains(@class,'header-link')]    # знаходить і чисто по text але я додала клас бо
# потрібні складні по завданню + може бути не одна така кнопка у майбутньому

# "Sign In" button on navigation panel
# 3) button.btn.header_signin
# 4)//button[text()='Sign In' and contains(@class,'header_signin')]
# (а як правильно всі класи вказувати якщо їх багато чи якшо з одним знаходить то цього достатньо?)

# "Sign up" button over the video
# 5) button.hero-descriptor_btn.btn.btn-primary
# 6) //button[text()='Sign up' and contains(@class,'hero-descriptor_btn')]

# Facebook icon
# 7) span.socials_icon.icon.icon-facebook
# 8) //span[contains(@class,'icon-facebook') and contains(@class,'socials_icon')]

# Telegram icon
# 9) a[href="https://t.me/ithillel_kyiv"].socials_link
# 10) //a[@href="https://t.me/ithillel_kyiv" and @class="socials_link"]

# ithillel.ua link
# 11) div a[href="https://ithillel.ua"].contacts_link.display-4
# 12) //a[@href="https://ithillel.ua" and text()="ithillel.ua"]

# support@ithillel.ua link
# 13) a[href="mailto:developer@ithillel.ua"].contacts_link.h4
# 14) //a[@href="mailto:developer@ithillel.ua" and text()="support@ithillel.ua"]

# image 1
# 47) div img[src="/assets/images/homepage/info_1.jpg"]
# 48) //div//img[@src="/assets/images/homepage/info_1.jpg"]

# "About" on navigation panel
# 49) nav button[appscrollto="aboutSection"]
# 50) //button[@appscrollto="aboutSection" and text()="About"]


# https://qauto2.forstudy.space/panel/garage page

# "My profile" user Nav Dropdow
# 15) div button#userNavDropdown
# 16) //div//button[@id="userNavDropdown"]

# Fuel expenses in "My profile" user Nav Dropdow  (using after "My profile" user Nav Dropdow click)
# 17) a[href="/panel/expenses"].dropdown-item.user-nav_link
# 18) //a[@href="/panel/expenses" and contains(@class, 'user-nav_link')]

# Instructions in "My profile" user Nav Dropdow (using after "My profile" user Nav Dropdow click)
# 19) a[href="/panel/instructions"].dropdown-item.user-nav_link
# 20) //a[@href="/panel/instructions" and text()="Instructions"]



# Log in modal

# Email input
# 21) div input#signinEmail[name="email"]
# 22) //div//input[@id="signinEmail"]


# Password input
# 23) div input#signinPassword[name="password"]
# 24) //div//input[@id="signinPassword"]

# Remember me checkbox
# 25) div input#remember
# 26) //div//input[@id="remember"]

# Forgot password link
# ---------------
# 27) //div//button[text()='Forgot password' and contains(@class,'btn-link')]

# Registration link
# ---------------
# 38) //div//button[text()='Registration' and contains(@class,'btn-link')]

# Login button
# 29) div button.btn-primary[type="button"]
# 30) //div//button[text()='Login' and contains(@class,'btn-primary')]

# Close modal
# 31) button.close
# 32) //button[span[text()="×"]]



# Sign up modal

# Name input
# 33) div input#signupName[name="name"]     # можна і без нейм по id ш без div якщо що)
# 34) //div//input[@id="signupName"]

# Last name input
# 35) div input#signupLastName[name="lastName"]
# 36) //div//input[@id="signupLastName"]

# Email input
# 37) div input#signupEmail[name="email"]
# 38) //div//input[@id="signupEmail"]

# Password input
# 39) div input#signupPassword[name="password"]
# 40) //div//input[@id="signupPassword"]

# Re-enter password input
# 41) div input#signupRepeatPassword[name="repeatPassword"]
# 42) //div//input[@id="signupRepeatPassword"]

# Register button
# 43) div button.btn-primary[type="button"]
# 44) //div//button[text()='Register' and contains(@class,'btn-primary')]

# Close modal icon
# 45) button.close
# 46) //button[span[text()="×"]]
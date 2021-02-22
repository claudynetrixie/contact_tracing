<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/claudynetrixie/contact_tracing">
    <img src="main/contact_tracing/static/images/circle.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Privatrace (Web App) </h3>

  <p align="center">
    A differentially-private contact tracing and indoor foot traffic system
    <br />
    <a href="https://github.com/claudynetrixie/contact_tracing"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Web Server</a></li>
        <li><a href="#built-with">Mobile Application</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
   
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p align = "center">
<img src="main/contact_tracing/static/images/splash_page.png" width="500" align = "center">
</p>

Privatrace seeks to strike a balance between both privacy and utility in implementing a contact tracing system. It involves a decentralized contact tracing approach paired with a differentially-private collection of foot traffic data. Privatrace conducts contact tracing without sharing users' data outside of their personal phones, and it uses differentially privatized data in foot traffic analysis to augment contact tracing efforts with insight into user movements to maximize the allocation of resources. Other than privacy and utility, strict user security was also implemented through the use of end-to-end encryption. This contact tracing system is composed an Android mobile application implemented using Java, a Web Application implemented using Django and AWS, and BLE beacons for location tracking.


### <ins>Web Server</ins>

The web server serves as the front-end for the aggregate report of the analyst and the back-end for functions mentioned below. 

Functions:
* Temporary API token
* Exposure Notifications
* Weekly Aggregate Report (Creation and Aggregation)


### Mobile Application
The mobile application plays an integral role in the contact tracing system proposed. It functions as the client facing portion of our system and will be the platform that the users can use to interact with the functions offered by our contact tracing system. Despite playing an external role in the system, the mobile application still contains a back-end and front-end portion, namely the database design and the mobile application functions. 

See the repo attached in the link below.

link: https://github.com/ps-balucan/CTeee

### Built With

The front-end of the web server is implemented using Django. On the other hand, its back-end is implemented using various Amazon Web Services (AWS) such as AWS Lambda for computation and processing, AWS Simple Notification Service (SNS) for push notifications, AWS Simple Queue Service (SQS) for queueing, AWS Cognito for user authentication and AWS API Gateway for API handling. Each function of the web server would be further described below.

* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Laravel](https://laravel.com)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```JS
   const API_KEY = 'ENTER YOUR API';
   ```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_







<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

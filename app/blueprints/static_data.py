static_data = {
    "sources": [
        {
            "id": "cnn",
            "country": "us",
            "articles": ["cnn1"],
            "name": "CNN",
            "description": "View the latest news and breaking news today for U.S., world, weather, entertainment, politics and health at CNN",
            "url": "http://us.cnn.com",
            "logoUrl": "http://i.newsapi.org/cnn-l.png",
        },
        {
            "id": "engadget",
            "country": "us",
            "articles": ["engadget1"],
            "name": "Engadget",
            "description": "Engadget is a web magazine with obsessive daily coverage of everything new in gadgets and consumer electronics.",
            "url": "https://www.engadget.com",
            "logoUrl": "http://i.newsapi.org/engadget-l.png",
        },
        {
            "id": "polygon",
            "country": "us",
            "articles": ["polygon1"],
            "name": "Polygon",
            "description": "Polygon is a gaming website in partnership with Vox Media. Our culture focused site covers games, their creators, the fans, trending stories and entertainment news.",
            "url": "http://www.polygon.com",
            "logoUrl": "http://i.newsapi.org/polygon-l.png"
        }
    ],
    "articles": [
        {
            "id": "cnn1",
            "source": "cnn",
            "countries": ["us"],
            "author": "Pamela Brown, Evan Perez and Shimon Prokupecz, CNN",
            "title": "US Officials: Info suggests Trump associates may have coordinated with Russians",
            "description": "The FBI has information that indicates associates of President Donald Trump communicated with suspected Russian operatives to possibly coordinate the release of information damaging to Hillary Clinton's campaign, US officials told CNN.",
            "url": "http://us.cnn.com/2017/03/22/politics/us-officials-info-suggests-trump-associates-may-have-coordinated-with-russians/index.html",
            "imageUrl": "http://i2.cdn.cnn.com/cnnnext/dam/assets/170320125707-05-comey-hearing-0320-super-tease.jpg",
            "publishDate": "2017-03-23T00:40:04Z"
        },
        {
            "id": "engadget1",
            "source": "engadget",
            "countries": ["us"],
            "author": "Jon Fingas",
            "title": "Apple acquisition hints at deep automation in iOS",
            "description": "Workflow can perform many tasks with a single tap.",
            "url": "https://www.engadget.com/2017/03/22/apple-acquires-workflow/",
            "imageUrl": "https://o.aolcdn.com/images/dims?thumbnail=1200%2C630&quality=80&image_uri=https%3A%2F%2Fs.aolcdn.com%2Fhss%2Fstorage%2Fmidas%2Fed04c4fa3fb986aa7e04741db428c222%2F205082311%2Fworkflow-ios.jpg&client=cbc79c14efcebee57402&signature=cec5d4b9bedd09bcf758410a3ea0827f69f962cb",
            "publishDate": "2017-03-23T03:03:00Z"
        },
        {
            "id": "polygon1",
            "source": "polygon",
            "countries": ["us"],
            "author": "Samit Sarkar",
            "title": "Red Dead Redemption being brought to PC — inside Grand Theft Auto 5",
            "description": "Good luck with the horses",
            "url": "http://www.polygon.com/2017/3/22/15027984/red-dead-redemption-v-pc-mod-grand-theft-auto",
            "imageUrl": "https://cdn0.vox-cdn.com/thumbor/G_ty6b63aIznZqUEfPfVMxXbBs8=/312x0:1919x904/1600x900/cdn0.vox-cdn.com/uploads/chorus_image/image/53841733/red_dead_redemption_v_screenshot_1919.0.jpg",
            "publishDate": "2017-03-22T22:00:02Z"
        }
    ],
    "countries": [
        {
            "id": "an",
            "sources": [],
            "articles": [],
            "name":"Andorra",
            "capital":"Andorra la Vella",
            "region":"Europe",
            "population": 78014,
            "flagUrl": "https://restcountries.eu/data/and.svg"
        },
        {
            "id": "ic",
            "sources": [],
            "articles": [],
            "name":"Iceland",
            "capital":"Reykjavík",
            "region":"Europe",
            "population":334300,
            "flagUrl": "https://restcountries.eu/data/isl.svg"
        },
        {
            "id": "us",
            "sources": ["cnn", "endgadget", "polygon"],
            "articles": ["cnn1", "engadget1", "polygon1"],
            "name":"United States of America",
            "capital":"Washington, D.C.",
            "region":"Americas",
            "population":323947000,
            "flagUrl": "https://restcountries.eu/data/usa.svg"
        }
    ]
}

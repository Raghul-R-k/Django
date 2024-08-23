from django.shortcuts import render

# Mock data
cards_data = [
    {'id': 1, 'card_title': 'Education', 'card_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consectetur tortor vel magna tincidunt tempus. Maecenas eget maximus eros. Vivamus id nisl lacus. Donec et risus turpis. In nec efficitur purus, ac faucibus nulla.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmCy16nhIbV3pI1qLYHMJKwbH2458oiC9EmA&s'},
    {'id': 2, 'card_title': 'Internships', 'card_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consectetur tortor vel magna tincidunt tempus. Maecenas eget maximus eros. Vivamus id nisl lacus. Donec et risus turpis. In nec efficitur purus, ac faucibus nulla.', 'image': 'https://images.ctfassets.net/hrltx12pl8hq/28ECAQiPJZ78hxatLTa7Ts/2f695d869736ae3b0de3e56ceaca3958/free-nature-images.jpg?fit=fill&w=1200&h=630'},
    {'id': 3, 'card_title': 'Projects', 'card_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consectetur tortor vel magna tincidunt tempus. Maecenas eget maximus eros. Vivamus id nisl lacus. Donec et risus turpis. In nec efficitur purus, ac faucibus nulla.', 'image': 'https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_1280.jpg'},
]

def land_page(request):
    section_name = 'About Me'
    return render(request, 'imgapp/index.html', {'section_name': section_name, 'cards': cards_data})


def second_page(request):
    return render(request, 'includes/cards.html', {'cards': cards_data})

def detail_page(request, card_id):
    for c in cards_data:
        if c['id'] == int(card_id):
            card = c
    return render(request, 'imgapp/detail.html', {'card': card})


interface Child {
  name: string;
  url: string;
}

export interface FooterNavData {
  title: string;
  childrens: Child[];
}

export const FOOTER_NAV_PRODUCT_DATA: FooterNavData[] = [
  {
    title: 'Product',
    childrens: [
      {
        name: 'About us',
        url: '/about',
      },
      {
        name: 'Contact us',
        url: '/contact',
      },
      {
        name: 'Terms of Service',
        url: '/terms',
      },
    ]
  },
  {
    title: 'Possibilities',
    childrens: [
      {
        name: 'How it work',
        url: '/how',
      },
      {
        name: 'Be a better streamer!',
        url: '/login',
      },
    ]
  }
]
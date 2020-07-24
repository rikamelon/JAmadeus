package com.chame.jamadeus;

import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.AccountType;

public class Jamadeus{
    private static String botToken = "BOT_TOKEN";

    public static void main(String[] args) throws Exception {
        new JDABuilder(AccountType.BOT).setToken(botToken).addEventListeners(new Listener()).build();
    }
}

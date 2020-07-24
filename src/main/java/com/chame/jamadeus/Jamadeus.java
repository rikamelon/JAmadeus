package com.chame.jamadeus;

import net.dv8tion.jda.api.AccountType;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.entities.Guild;
import net.dv8tion.jda.api.entities.TextChannel;
import net.dv8tion.jda.api.entities.VoiceChannel;
import net.dv8tion.jda.api.events.message.guild.GuildMessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import net.dv8tion.jda.api.managers.AudioManager;

import java.util.HashMap;
import java.util.Map;

public class Jamadeus{
    private static String botToken = "BOT_TOKEN";

    public static void main(String[] args) throws Exception {
      new JDABuilder(AccountType.BOT).setToken(botToken).addEventListeners(new Listener()).build();
    }
}